'use client'

import { useRef, useEffect, useCallback } from 'react'
import { useChat } from '@ai-sdk/react'
import { DefaultChatTransport } from 'ai'
import { ChatMessage, TypingIndicator } from './chat-message'
import { ChatInput } from './chat-input'
import type { ContentStrictnessLevel, RawanDialect } from '@/lib/rawan-prompts'
import { Bot } from 'lucide-react'

interface ChatInterfaceProps {
  strictness: ContentStrictnessLevel
  dialect: RawanDialect
}

export function ChatInterface({ strictness, dialect }: ChatInterfaceProps) {
  const scrollRef = useRef<HTMLDivElement>(null)

  const { messages, sendMessage, status, stop } = useChat({
    transport: new DefaultChatTransport({
      api: '/api/chat',
      prepareSendMessagesRequest: ({ id, messages }) => ({
        body: {
          messages,
          id,
          strictness,
          dialect,
        },
      }),
    }),
  })

  const isLoading = status === 'streaming' || status === 'submitted'

  const handleSend = useCallback(
    (text: string) => sendMessage({ text }),
    [sendMessage]
  )

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight
    }
  }, [messages, isLoading])

  return (
    <div className="flex flex-col h-full">
      {/* Messages Area */}
      <div
        ref={scrollRef}
        className="flex-1 overflow-y-auto scrollbar-thin p-4"
      >
        <div className="max-w-3xl mx-auto flex flex-col gap-6">
          {messages.length === 0 && <WelcomeScreen onSuggestion={handleSend} />}

          {messages.map((message) => (
            <ChatMessage key={message.id} message={message} />
          ))}

          {status === 'submitted' && <TypingIndicator />}
        </div>
      </div>

      {/* Input Area */}
      <ChatInput
        onSend={handleSend}
        onStop={stop}
        isLoading={isLoading}
      />
    </div>
  )
}

function WelcomeScreen({ onSuggestion }: { onSuggestion: (text: string) => void }) {
  const suggestions = [
    'ساعديني أنظم يومي',
    'أبغى نصيحة عن عادات صحية',
    'كيف أحسن إنتاجيتي؟',
    'أبغى أتعلم شي جديد',
  ]

  return (
    <div className="flex flex-col items-center justify-center py-16 gap-6">
      <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-primary/15 text-primary animate-pulse-glow">
        <Bot className="h-8 w-8" />
      </div>
      <div className="text-center">
        <h2 className="text-xl font-semibold text-foreground text-balance">
          هلا بك، أنا روان
        </h2>
        <p className="text-sm text-muted-foreground mt-2 max-w-md text-pretty">
          وكيلتك الذكية للمساعدة اليومية. اسألني أي شي أو اختر من الاقتراحات
        </p>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 w-full max-w-md">
        {suggestions.map((suggestion) => (
          <button
            key={suggestion}
            className="rounded-xl border border-border bg-card px-4 py-3 text-sm text-card-foreground hover:bg-secondary/80 transition-colors text-start"
            onClick={() => onSuggestion(suggestion)}
          >
            {suggestion}
          </button>
        ))}
      </div>
    </div>
  )
}
