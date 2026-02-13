'use client'

import { cn } from '@/lib/utils'
import type { UIMessage } from 'ai'
import { Bot, User } from 'lucide-react'

function getMessageText(message: UIMessage): string {
  if (!message.parts || !Array.isArray(message.parts)) return ''
  return message.parts
    .filter((p): p is { type: 'text'; text: string } => p.type === 'text')
    .map((p) => p.text)
    .join('')
}

export function ChatMessage({ message }: { message: UIMessage }) {
  const isUser = message.role === 'user'
  const text = getMessageText(message)

  return (
    <div
      className={cn(
        'flex gap-3 items-start',
        isUser ? 'flex-row-reverse' : 'flex-row'
      )}
    >
      <div
        className={cn(
          'flex h-8 w-8 shrink-0 items-center justify-center rounded-lg',
          isUser
            ? 'bg-primary/20 text-primary'
            : 'bg-accent/20 text-accent animate-pulse-glow'
        )}
        aria-hidden="true"
      >
        {isUser ? <User className="h-4 w-4" /> : <Bot className="h-4 w-4" />}
      </div>
      <div
        className={cn(
          'flex flex-col gap-1 max-w-[80%]',
          isUser ? 'items-end' : 'items-start'
        )}
      >
        <span className="text-xs text-muted-foreground">
          {isUser ? 'أنت' : 'روان'}
        </span>
        <div
          className={cn(
            'rounded-2xl px-4 py-3 text-sm leading-relaxed whitespace-pre-wrap',
            isUser
              ? 'bg-primary text-primary-foreground rounded-br-sm'
              : 'bg-card border border-border text-card-foreground rounded-bl-sm'
          )}
        >
          {text}
        </div>
      </div>
    </div>
  )
}

export function TypingIndicator() {
  return (
    <div className="flex gap-3 items-start">
      <div
        className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-accent/20 text-accent animate-pulse-glow"
        aria-hidden="true"
      >
        <Bot className="h-4 w-4" />
      </div>
      <div className="flex flex-col gap-1 items-start">
        <span className="text-xs text-muted-foreground">روان</span>
        <div className="rounded-2xl rounded-bl-sm bg-card border border-border px-4 py-3">
          <div className="flex gap-1.5 items-center" role="status" aria-label="روان تكتب">
            <span className="sr-only">روان تكتب...</span>
            <span
              className="h-2 w-2 rounded-full bg-muted-foreground/60 animate-bounce"
              style={{ animationDelay: '0ms' }}
            />
            <span
              className="h-2 w-2 rounded-full bg-muted-foreground/60 animate-bounce"
              style={{ animationDelay: '150ms' }}
            />
            <span
              className="h-2 w-2 rounded-full bg-muted-foreground/60 animate-bounce"
              style={{ animationDelay: '300ms' }}
            />
          </div>
        </div>
      </div>
    </div>
  )
}
