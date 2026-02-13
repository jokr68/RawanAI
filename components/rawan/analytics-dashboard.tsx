'use client'

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import {
  Activity,
  TrendingUp,
  Brain,
  Target,
  Flame,
  BarChart3,
} from 'lucide-react'

// Demo data for the analytics view
const WEEK_DATA = [
  { day: 'سبت', habits: 4, total: 4, mood: 5 },
  { day: 'أحد', habits: 3, total: 4, mood: 4 },
  { day: 'اثنين', habits: 4, total: 4, mood: 5 },
  { day: 'ثلاثاء', habits: 2, total: 4, mood: 3 },
  { day: 'أربعاء', habits: 3, total: 4, mood: 4 },
  { day: 'خميس', habits: 1, total: 4, mood: 2 },
  { day: 'جمعة', habits: 4, total: 4, mood: 5 },
]

function MiniBar({ value, max }: { value: number; max: number }) {
  const pct = (value / max) * 100
  return (
    <div className="flex flex-col items-center gap-1">
      <div className="w-8 h-20 bg-secondary/50 rounded-full overflow-hidden flex flex-col-reverse">
        <div
          className="w-full bg-primary rounded-full transition-all duration-500"
          style={{ height: `${pct}%` }}
        />
      </div>
    </div>
  )
}

export function AnalyticsDashboard() {
  const totalHabitsThisWeek = WEEK_DATA.reduce((s, d) => s + d.habits, 0)
  const totalPossible = WEEK_DATA.reduce((s, d) => s + d.total, 0)
  const weeklyRate = Math.round((totalHabitsThisWeek / totalPossible) * 100)
  const avgMood = (
    WEEK_DATA.reduce((s, d) => s + d.mood, 0) / WEEK_DATA.length
  ).toFixed(1)
  const bestStreak = 12

  return (
    <div className="flex flex-col gap-6 p-6 max-w-2xl mx-auto">
      {/* KPI Cards */}
      <div className="grid grid-cols-2 gap-3">
        <Card className="bg-card border-border">
          <CardContent className="flex flex-col gap-2 p-4">
            <div className="flex items-center gap-2 text-muted-foreground">
              <Target className="h-4 w-4 text-primary" />
              <span className="text-xs">إنجاز الأسبوع</span>
            </div>
            <span className="text-2xl font-bold text-foreground">
              {weeklyRate}%
            </span>
            <Badge variant="secondary" className="w-fit text-xs">
              <TrendingUp className="h-3 w-3 ml-1" />
              +5% من الأسبوع الماضي
            </Badge>
          </CardContent>
        </Card>

        <Card className="bg-card border-border">
          <CardContent className="flex flex-col gap-2 p-4">
            <div className="flex items-center gap-2 text-muted-foreground">
              <Activity className="h-4 w-4 text-accent" />
              <span className="text-xs">متوسط المزاج</span>
            </div>
            <span className="text-2xl font-bold text-foreground">
              {avgMood}/5
            </span>
            <Badge variant="secondary" className="w-fit text-xs">
              حالة ممتازة
            </Badge>
          </CardContent>
        </Card>

        <Card className="bg-card border-border">
          <CardContent className="flex flex-col gap-2 p-4">
            <div className="flex items-center gap-2 text-muted-foreground">
              <Flame className="h-4 w-4 text-orange-400" />
              <span className="text-xs">أطول سلسلة</span>
            </div>
            <span className="text-2xl font-bold text-foreground">
              {bestStreak} يوم
            </span>
            <Badge variant="secondary" className="w-fit text-xs">
              القراءة
            </Badge>
          </CardContent>
        </Card>

        <Card className="bg-card border-border">
          <CardContent className="flex flex-col gap-2 p-4">
            <div className="flex items-center gap-2 text-muted-foreground">
              <BarChart3 className="h-4 w-4 text-green-400" />
              <span className="text-xs">عادات مكتملة</span>
            </div>
            <span className="text-2xl font-bold text-foreground">
              {totalHabitsThisWeek}/{totalPossible}
            </span>
            <Badge variant="secondary" className="w-fit text-xs">
              هذا الأسبوع
            </Badge>
          </CardContent>
        </Card>
      </div>

      {/* Weekly Chart */}
      <Card className="bg-card border-border">
        <CardHeader>
          <CardTitle className="text-sm flex items-center gap-2">
            <BarChart3 className="h-4 w-4 text-primary" />
            إنجاز العادات اليومي
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex items-end justify-between gap-2">
            {WEEK_DATA.map((d) => (
              <div key={d.day} className="flex flex-col items-center gap-2">
                <MiniBar value={d.habits} max={d.total} />
                <span className="text-xs text-muted-foreground">{d.day}</span>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* AI Insight */}
      <Card className="bg-primary/5 border-primary/20">
        <CardContent className="flex gap-4 p-4">
          <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-primary/20 text-primary">
            <Brain className="h-5 w-5" />
          </div>
          <div className="flex flex-col gap-1">
            <span className="font-medium text-sm text-foreground">
              رؤية روان
            </span>
            <p className="text-sm text-muted-foreground leading-relaxed">
              لاحظت إن إنتاجيتك تنخفض يوم الخميس عادةً. جرب تخفف المهام في هاليوم وتركز على الراحة عشان تبدأ الجمعة بنشاط أكبر.
            </p>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
