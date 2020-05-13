class PubSubService:
	subscribers_topic_map: Dict[str, set] = {}
	messages_queue: List = []

	def add_message_to_queue(message):
		messages_queue.append(message)

	def add_subscriber(topic: str, subscriber: Subscriber):
		if topic in subscribers_topic_map:
      subscribers_topic_map[topic].insert(subscriber)
		else:
      subscribers_topic_map[topic] = {subscriber}

	def broadcast(self):
        if not messages_queue:
            print("No messages from publishers to display")
        else:
			while messages_queue:
				message = messages_queue.pop()
				topic = message.get_topic()

				subscribers_of_topic: Set = subscribers_topic_map.get(topic)

				for subscriber in subscribers_topic_map.get(topic):
					subscriber.messages

	//Sends messages about a topic for subscriber at any point
	public void getMessagesForSubscriberOfTopic(String topic, Subscriber subscriber) {
		if(messages_queue.isEmpty()){
			System.out.println("No messages from publishers to display");
		}else{
			while(!messages_queue.isEmpty()){
				Message message = messages_queue.remove();

				if(message.getTopic().equalsIgnoreCase(topic)){

					Set<Subscriber> subscribers_of_topic = subscribersTopicMap.get(topic);

					for(Subscriber _subscriber : subscribers_of_topic){
						if(_subscriber.equals(subscriber)){
							//add broadcasted message to subscriber message queue
							List<Message> subscriber_messages = subscriber.getsubscriber_messages();
							subscriber_messages.add(message);
							subscriber.setsubscriber_messages(subscriber_messages);
