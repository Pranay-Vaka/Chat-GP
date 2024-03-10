"use client"

import React, { FC, FormEventHandler, useState } from 'react'
import { MessageData } from '@/api'

type Props = {
  messagesData: MessageData[],
  topic: string
}

const ChatSection: FC<Props> = ({ messagesData, topic }) => {
  const [messages, setMessages] = useState(messagesData);
  const [input, setInput] = useState("");

  const sendMessage: FormEventHandler<HTMLFormElement> = (e) => {
    e.preventDefault();

    if (input.trim() === "") return;

    setMessages([...messages, {
      model: "chat-gp.message",
      pk: messages.length + 1,
      fields: {
        user: 1,
        forum: 1,
        content: input,
        time_stamp: new Date().toISOString()
      }
    }]);
    setInput("");
  }

  return (
    <div className='card w-full h-full shadow-xl'>
      <div className='card-body'>
        <h2 className='card-title text-black'>Chat</h2>
        <div className="chat chat-start">
          <div className="chat-header">
            {topic.split("%20").join(" ")} channel
            <time className="text-xs opacity-50 ml-1">{new Date('2024-03-07T09:11:00').toUTCString()}</time>
          </div>
          <div className="chat-bubble bg-white text-black">
            Welcome to the <span className='font-bold'>{topic.split("%20").join(" ")}</span> discussion channel! Please remember to always be respectful and exercise kindness where you can.
          </div>
        </div>

        {messages.map((message) => (
          <div key={`${message.model}${message.pk}`} className="chat chat-end">
            <div className="chat-header">
              SamSoong
              <time className="text-xs opacity-50 ml-1">{new Date(message.fields.time_stamp).toUTCString()}</time>
            </div>
            <div className="chat-bubble bg-blue-500 text-white">{message.fields.content}</div>
          </div>
        ))}

        <div className='mt-auto'></div>
        <form onSubmit={sendMessage}>
          <input type="text" placeholder="Send a message" className="input input-bordered w-full" value={input} onChange={(e) => setInput(e.target.value)} />
        </form>
      </div>
    </div>
  )
}

export default ChatSection
