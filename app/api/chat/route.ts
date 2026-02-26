import {
  consumeStream,
  convertToModelMessages,
  streamText,
  type UIMessage,
} from 'ai'
import {
  buildSystemPrompt,
  type ContentStrictnessLevel,
  type RawanDialect,
} from '@/lib/rawan-prompts'

export const maxDuration = 30

export async function POST(req: Request) {
  const {
    messages,
    strictness = 'balanced',
    dialect = 'jeddawi',
  }: {
    messages: UIMessage[]
    strictness?: ContentStrictnessLevel
    dialect?: RawanDialect
  } = await req.json()

  const systemPrompt = buildSystemPrompt({
    contentStrictness: strictness,
    dialect,
  })

  const result = streamText({
    model: 'anthropic/claude-sonnet-4-20250514',
    system: systemPrompt,
    messages: await convertToModelMessages(messages),
    abortSignal: req.signal,
  })

  return result.toUIMessageStreamResponse({
    originalMessages: messages,
    consumeSseStream: consumeStream,
  })
}
