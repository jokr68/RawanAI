'use client'

import { useState } from 'react'
import { ChatInterface } from '@/components/rawan/chat-interface'
import { SettingsPanel } from '@/components/rawan/settings-panel'
import { HabitsTracker } from '@/components/rawan/habits-tracker'
import { AnalyticsDashboard } from '@/components/rawan/analytics-dashboard'
import { Button } from '@/components/ui/button'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Separator } from '@/components/ui/separator'
import type {
  ContentStrictnessLevel,
  RawanDialect,
} from '@/lib/rawan-prompts'
import {
  Bot,
  MessageCircle,
  BarChart3,
  Target,
  Settings,
  PanelRightOpen,
  PanelRightClose,
} from 'lucide-react'

type View = 'chat' | 'habits' | 'analytics' | 'settings'

const NAV_ITEMS: { id: View; label: string; icon: React.ReactNode }[] = [
  {
    id: 'chat',
    label: 'المحادثة',
    icon: <MessageCircle className="h-5 w-5" />,
  },
  {
    id: 'habits',
    label: 'العادات',
    icon: <Target className="h-5 w-5" />,
  },
  {
    id: 'analytics',
    label: 'التحليلات',
    icon: <BarChart3 className="h-5 w-5" />,
  },
  {
    id: 'settings',
    label: 'الإعدادات',
    icon: <Settings className="h-5 w-5" />,
  },
]

export default function RawanPage() {
  const [activeView, setActiveView] = useState<View>('chat')
  const [sidebarOpen, setSidebarOpen] = useState(true)
  const [strictness, setStrictness] =
    useState<ContentStrictnessLevel>('balanced')
  const [dialect, setDialect] = useState<RawanDialect>('jeddawi')

  return (
    <div className="flex h-dvh bg-background overflow-hidden">
      {/* Sidebar */}
      <aside
        className={`flex flex-col border-l border-border bg-card transition-all duration-300 ${
          sidebarOpen ? 'w-60' : 'w-0 overflow-hidden'
        } md:relative absolute inset-y-0 right-0 z-20`}
      >
        {/* Logo */}
        <div className="flex items-center gap-3 p-4 h-16">
          <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-primary/15 text-primary">
            <Bot className="h-5 w-5" />
          </div>
          <div className="flex flex-col">
            <span className="font-bold text-foreground text-sm">RawanAI</span>
            <span className="text-xs text-muted-foreground">
              وكيلتك الذكية
            </span>
          </div>
        </div>

        <Separator />

        {/* Navigation */}
        <ScrollArea className="flex-1 p-3">
          <nav className="flex flex-col gap-1" aria-label="التنقل الرئيسي">
            {NAV_ITEMS.map((item) => (
              <Button
                key={item.id}
                variant={activeView === item.id ? 'secondary' : 'ghost'}
                className={`justify-start gap-3 h-11 ${
                  activeView === item.id
                    ? 'bg-primary/10 text-primary font-medium'
                    : 'text-muted-foreground hover:text-foreground'
                }`}
                onClick={() => setActiveView(item.id)}
                aria-current={activeView === item.id ? 'page' : undefined}
              >
                {item.icon}
                <span>{item.label}</span>
              </Button>
            ))}
          </nav>
        </ScrollArea>

        {/* Sidebar Footer */}
        <div className="p-4 border-t border-border">
          <div className="flex items-center gap-3 rounded-xl bg-secondary/50 p-3">
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary/20 text-primary text-sm font-bold">
              م
            </div>
            <div className="flex flex-col min-w-0">
              <span className="text-sm font-medium text-foreground truncate">
                مستخدم
              </span>
              <span className="text-xs text-muted-foreground">الخطة المجانية</span>
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col min-w-0">
        {/* Top Bar */}
        <header className="flex items-center gap-3 h-16 px-4 border-b border-border bg-background shrink-0">
          <Button
            variant="ghost"
            size="icon"
            className="h-9 w-9"
            onClick={() => setSidebarOpen(!sidebarOpen)}
            aria-label={sidebarOpen ? 'إغلاق القائمة' : 'فتح القائمة'}
          >
            {sidebarOpen ? (
              <PanelRightClose className="h-5 w-5" />
            ) : (
              <PanelRightOpen className="h-5 w-5" />
            )}
          </Button>

          <h1 className="text-sm font-semibold text-foreground">
            {NAV_ITEMS.find((i) => i.id === activeView)?.label}
          </h1>

          {activeView === 'chat' && (
            <div className="flex items-center gap-2 mr-auto">
              <span className="text-xs text-muted-foreground hidden sm:inline">
                الصرامة:
              </span>
              <span className="text-xs font-medium text-primary">
                {strictness === 'strict'
                  ? 'صارم'
                  : strictness === 'balanced'
                  ? 'متوازن'
                  : strictness === 'relaxed'
                  ? 'مرن'
                  : 'متحرر'}
              </span>
            </div>
          )}
        </header>

        {/* Content Area */}
        <div className="flex-1 min-h-0">
          {activeView === 'chat' && (
            <ChatInterface strictness={strictness} dialect={dialect} />
          )}
          {activeView === 'habits' && <HabitsTracker />}
          {activeView === 'analytics' && (
            <ScrollArea className="h-full">
              <AnalyticsDashboard />
            </ScrollArea>
          )}
          {activeView === 'settings' && (
            <ScrollArea className="h-full">
              <SettingsPanel
                strictness={strictness}
                dialect={dialect}
                onStrictnessChange={setStrictness}
                onDialectChange={setDialect}
              />
            </ScrollArea>
          )}
        </div>
      </main>

      {/* Mobile Overlay */}
      {sidebarOpen && (
        <div
          className="md:hidden fixed inset-0 bg-background/80 backdrop-blur-sm z-10"
          onClick={() => setSidebarOpen(false)}
          aria-hidden="true"
        />
      )}
    </div>
  )
}
