package com.omega.on.producer;

import org.apache.kafka.clients.admin.NewTopic;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.ApplicationListener;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.integration.dsl.IntegrationFlow;
import org.springframework.integration.dsl.MessageChannels;
import org.springframework.integration.kafka.dsl.Kafka;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.core.ProducerFactory;
import org.springframework.kafka.support.converter.JsonMessageConverter;
import org.springframework.kafka.support.serializer.JsonSerializer;
import org.springframework.messaging.Message;
import org.springframework.messaging.MessageChannel;
import org.springframework.messaging.support.MessageBuilder;

import java.util.Map;
import java.util.Random;


import static com.omega.on.producer.ProducerApplication.OMEGAON_VIEWS_TOPIC;

@SpringBootApplication
public class ProducerApplication {

	public static void main(String[] args) {
		SpringApplication.run(ProducerApplication.class, args);
	}

	final static String OMEGAON_VIEWS_TOPIC = "omegaon.test.topic";
}

@Configuration
class RunnerConfiguration{

	void kafka (KafkaTemplate <Object,Object> template){
		var pageView = (PageView) random("kafka");
		template.send(OMEGAON_VIEWS_TOPIC, pageView);
	}

	private PageView random(String source) {
		var names = "pepe,lola,mar,lolo".split(",");
		var pages = "log,about,index,contact".split(",");
		var random = new Random();
		var name = names[random.nextInt(names.length)];
		var page = pages[random.nextInt(pages.length)];
		return new PageView(page, Math.random() > .5 ? 100 : 1000, name, source);
	}

	void integration(MessageChannel channel){
		var message = MessageBuilder
				.withPayload(random("integration"))
				.build();

		channel.send(message);
	}

	@Bean
	ApplicationListener <ApplicationReadyEvent> runnerListener (KafkaTemplate<Object,Object> template, MessageChannel channel){
		return event -> {
            //kafka(template);
            integration(channel);
        };
	}
}

@Configuration
class IntegrationConfiguration {

	@Bean
	IntegrationFlow flow(MessageChannel channel, KafkaTemplate<Object,Object> template){
		var kafka = Kafka
				.outboundChannelAdapter(template)
				.topic(OMEGAON_VIEWS_TOPIC)
				.getObject();
		return IntegrationFlow
				.from(channel)
				.handle(kafka)
				.get();
	}

	@Bean
	MessageChannel channel(){
		return MessageChannels.direct().getObject();
	}
}


@Configuration
class KafkaConfiguration{

	@KafkaListener(topics = OMEGAON_VIEWS_TOPIC, groupId = "omegaon_topic_group")
	public void onNewOmegaView(Message<PageView> pageView){
		System.out.printf("--------------------");
		System.out.println("new page view listener " + pageView.getPayload());
		pageView.getHeaders().forEach((s,o) -> System.out.println(s +"=" + o));

	}

	@Bean
	NewTopic omegaOnTopic(){
		return new NewTopic(OMEGAON_VIEWS_TOPIC, 1, (short)1);
	}

	@Bean
	JsonMessageConverter jsonMessageConverter(){
		return new JsonMessageConverter();
	}

	@Bean
	KafkaTemplate<Object,Object> kafkaTemplate(ProducerFactory<Object, Object> producerFactory){
		return new KafkaTemplate<>(producerFactory,
				Map.of(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, JsonSerializer.class));
	}
}

record PageView(String page,long Duration, String userId, String source){}
