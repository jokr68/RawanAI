'use client'

import {
  STRICTNESS_LABELS,
  DIALECT_LABELS,
  type ContentStrictnessLevel,
  type RawanDialect,
} from '@/lib/rawan-prompts'
import { Label } from '@/components/ui/label'
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group'
import { Badge } from '@/components/ui/badge'
import { Shield, ShieldAlert, ShieldOff, ShieldCheck, MessageCircle } from 'lucide-react'

const STRICTNESS_ICONS: Record<ContentStrictnessLevel, React.ReactNode> = {
  strict: <ShieldCheck className="h-4 w-4" />,
  balanced: <Shield className="h-4 w-4" />,
  relaxed: <ShieldAlert className="h-4 w-4" />,
  unrestricted: <ShieldOff className="h-4 w-4" />,
}

interface SettingsPanelProps {
  strictness: ContentStrictnessLevel
  dialect: RawanDialect
  onStrictnessChange: (level: ContentStrictnessLevel) => void
  onDialectChange: (dialect: RawanDialect) => void
}

export function SettingsPanel({
  strictness,
  dialect,
  onStrictnessChange,
  onDialectChange,
}: SettingsPanelProps) {
  return (
    <div className="flex flex-col gap-8 p-6 max-w-2xl mx-auto">
      <div>
        <h2 className="text-lg font-semibold text-foreground flex items-center gap-2">
          <Shield className="h-5 w-5 text-primary" />
          مستوى صرامة المحتوى
        </h2>
        <p className="text-sm text-muted-foreground mt-1">
          تحكم في مدى تقييد ردود روان للمحتوى
        </p>
      </div>

      <RadioGroup
        value={strictness}
        onValueChange={(v) => onStrictnessChange(v as ContentStrictnessLevel)}
        className="flex flex-col gap-3"
      >
        {(
          Object.entries(STRICTNESS_LABELS) as [
            ContentStrictnessLevel,
            { ar: string; description: string },
          ][]
        ).map(([key, { ar, description }]) => (
          <Label
            key={key}
            htmlFor={`strictness-${key}`}
            className={`flex items-start gap-4 rounded-xl border p-4 cursor-pointer transition-all ${
              strictness === key
                ? 'border-primary bg-primary/5'
                : 'border-border bg-card hover:bg-secondary/50'
            }`}
          >
            <RadioGroupItem
              value={key}
              id={`strictness-${key}`}
              className="mt-0.5"
            />
            <div className="flex flex-col gap-1 flex-1">
              <div className="flex items-center gap-2">
                {STRICTNESS_ICONS[key]}
                <span className="font-medium text-foreground">{ar}</span>
                {key === 'balanced' && (
                  <Badge variant="secondary" className="text-xs">
                    افتراضي
                  </Badge>
                )}
              </div>
              <span className="text-sm text-muted-foreground">
                {description}
              </span>
            </div>
          </Label>
        ))}
      </RadioGroup>

      <div className="border-t border-border pt-8">
        <h2 className="text-lg font-semibold text-foreground flex items-center gap-2">
          <MessageCircle className="h-5 w-5 text-accent" />
          لهجة روان
        </h2>
        <p className="text-sm text-muted-foreground mt-1">
          اختر اللهجة التي تفضل أن تتحدث بها روان
        </p>
      </div>

      <RadioGroup
        value={dialect}
        onValueChange={(v) => onDialectChange(v as RawanDialect)}
        className="flex flex-col gap-3"
      >
        {(
          Object.entries(DIALECT_LABELS) as [
            RawanDialect,
            { ar: string; description: string },
          ][]
        ).map(([key, { ar, description }]) => (
          <Label
            key={key}
            htmlFor={`dialect-${key}`}
            className={`flex items-start gap-4 rounded-xl border p-4 cursor-pointer transition-all ${
              dialect === key
                ? 'border-accent bg-accent/5'
                : 'border-border bg-card hover:bg-secondary/50'
            }`}
          >
            <RadioGroupItem
              value={key}
              id={`dialect-${key}`}
              className="mt-0.5"
            />
            <div className="flex flex-col gap-1">
              <span className="font-medium text-foreground">{ar}</span>
              <span className="text-sm text-muted-foreground">
                {description}
              </span>
            </div>
          </Label>
        ))}
      </RadioGroup>
    </div>
  )
}
