'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Progress } from '@/components/ui/progress'
import { Badge } from '@/components/ui/badge'
import {
  Plus,
  Check,
  Flame,
  Droplets,
  BookOpen,
  Dumbbell,
  Moon,
  Brain,
  X,
  Target,
} from 'lucide-react'

interface Habit {
  id: string
  name: string
  icon: string
  completedToday: boolean
  streak: number
  color: string
}

const ICON_MAP: Record<string, React.ReactNode> = {
  flame: <Flame className="h-5 w-5" />,
  droplets: <Droplets className="h-5 w-5" />,
  book: <BookOpen className="h-5 w-5" />,
  dumbbell: <Dumbbell className="h-5 w-5" />,
  moon: <Moon className="h-5 w-5" />,
  brain: <Brain className="h-5 w-5" />,
  target: <Target className="h-5 w-5" />,
}

const PRESET_HABITS = [
  { name: 'شرب الماء', icon: 'droplets', color: 'text-blue-400' },
  { name: 'التمارين', icon: 'dumbbell', color: 'text-green-400' },
  { name: 'القراءة', icon: 'book', color: 'text-amber-400' },
  { name: 'النوم المبكر', icon: 'moon', color: 'text-indigo-400' },
  { name: 'التأمل', icon: 'brain', color: 'text-pink-400' },
]

const DEFAULT_HABITS: Habit[] = [
  { id: '1', name: 'شرب الماء', icon: 'droplets', completedToday: false, streak: 3, color: 'text-blue-400' },
  { id: '2', name: 'التمارين', icon: 'dumbbell', completedToday: false, streak: 7, color: 'text-green-400' },
  { id: '3', name: 'القراءة', icon: 'book', completedToday: false, streak: 12, color: 'text-amber-400' },
  { id: '4', name: 'النوم المبكر', icon: 'moon', completedToday: false, streak: 2, color: 'text-indigo-400' },
]

export function HabitsTracker() {
  const [habits, setHabits] = useState<Habit[]>(DEFAULT_HABITS)
  const [showAdd, setShowAdd] = useState(false)
  const [newHabitName, setNewHabitName] = useState('')
  const [selectedIcon, setSelectedIcon] = useState('target')

  const completedCount = habits.filter((h) => h.completedToday).length
  const progress = habits.length > 0 ? (completedCount / habits.length) * 100 : 0

  const toggleHabit = (id: string) => {
    setHabits((prev) =>
      prev.map((h) =>
        h.id === id
          ? {
              ...h,
              completedToday: !h.completedToday,
              streak: !h.completedToday ? h.streak + 1 : h.streak - 1,
            }
          : h
      )
    )
  }

  const addHabit = () => {
    if (!newHabitName.trim()) return
    const preset = PRESET_HABITS.find((p) => p.icon === selectedIcon)
    setHabits((prev) => [
      ...prev,
      {
        id: Date.now().toString(),
        name: newHabitName.trim(),
        icon: selectedIcon,
        completedToday: false,
        streak: 0,
        color: preset?.color || 'text-primary',
      },
    ])
    setNewHabitName('')
    setShowAdd(false)
  }

  const removeHabit = (id: string) => {
    setHabits((prev) => prev.filter((h) => h.id !== id))
  }

  return (
    <div className="flex flex-col gap-6 p-6 max-w-2xl mx-auto">
      {/* Progress Header */}
      <Card className="bg-card border-border">
        <CardHeader className="pb-3">
          <CardTitle className="text-lg flex items-center justify-between">
            <span className="flex items-center gap-2">
              <Target className="h-5 w-5 text-primary" />
              تقدم اليوم
            </span>
            <Badge variant="secondary" className="text-sm">
              {completedCount}/{habits.length}
            </Badge>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <Progress value={progress} className="h-3" />
          <p className="text-sm text-muted-foreground mt-2">
            {progress === 100
              ? 'ممتاز! أكملت جميع عاداتك اليوم'
              : progress > 50
              ? 'أحسنت! كملي على هالمنوال'
              : progress > 0
              ? 'بداية حلوة، كمّل!'
              : 'ابدأ يومك بإنجاز عادة واحدة'}
          </p>
        </CardContent>
      </Card>

      {/* Habits List */}
      <div className="flex flex-col gap-3">
        {habits.map((habit) => (
          <Card
            key={habit.id}
            className={`bg-card border transition-all ${
              habit.completedToday
                ? 'border-primary/40 bg-primary/5'
                : 'border-border'
            }`}
          >
            <CardContent className="flex items-center gap-4 p-4">
              <button
                onClick={() => toggleHabit(habit.id)}
                className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-xl transition-all ${
                  habit.completedToday
                    ? 'bg-primary text-primary-foreground'
                    : `bg-secondary/50 ${habit.color}`
                }`}
                aria-label={
                  habit.completedToday
                    ? `إلغاء إتمام ${habit.name}`
                    : `إتمام ${habit.name}`
                }
              >
                {habit.completedToday ? (
                  <Check className="h-5 w-5" />
                ) : (
                  ICON_MAP[habit.icon] || <Target className="h-5 w-5" />
                )}
              </button>
              <div className="flex flex-col flex-1 min-w-0">
                <span
                  className={`font-medium text-sm ${
                    habit.completedToday
                      ? 'line-through text-muted-foreground'
                      : 'text-foreground'
                  }`}
                >
                  {habit.name}
                </span>
                <span className="text-xs text-muted-foreground flex items-center gap-1">
                  <Flame className="h-3 w-3 text-orange-400" />
                  {habit.streak} يوم متتالي
                </span>
              </div>
              <Button
                variant="ghost"
                size="icon"
                className="h-8 w-8 text-muted-foreground hover:text-destructive"
                onClick={() => removeHabit(habit.id)}
                aria-label={`حذف ${habit.name}`}
              >
                <X className="h-4 w-4" />
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Add Habit */}
      {showAdd ? (
        <Card className="bg-card border-border">
          <CardContent className="flex flex-col gap-4 p-4">
            <Input
              value={newHabitName}
              onChange={(e) => setNewHabitName(e.target.value)}
              placeholder="اسم العادة..."
              className="bg-secondary/50 border-border"
              autoFocus
              onKeyDown={(e) => e.key === 'Enter' && addHabit()}
            />
            <div className="flex gap-2 flex-wrap">
              {Object.entries(ICON_MAP).map(([key, icon]) => (
                <button
                  key={key}
                  onClick={() => setSelectedIcon(key)}
                  className={`flex h-10 w-10 items-center justify-center rounded-lg transition-all ${
                    selectedIcon === key
                      ? 'bg-primary text-primary-foreground'
                      : 'bg-secondary/50 text-muted-foreground hover:text-foreground'
                  }`}
                  aria-label={`اختر أيقونة ${key}`}
                >
                  {icon}
                </button>
              ))}
            </div>
            <div className="flex gap-2">
              <Button onClick={addHabit} className="flex-1" disabled={!newHabitName.trim()}>
                إضافة
              </Button>
              <Button
                variant="outline"
                onClick={() => setShowAdd(false)}
                className="flex-1"
              >
                إلغاء
              </Button>
            </div>
          </CardContent>
        </Card>
      ) : (
        <Button
          variant="outline"
          className="border-dashed border-2 h-12"
          onClick={() => setShowAdd(true)}
        >
          <Plus className="h-4 w-4 ml-2" />
          إضافة عادة جديدة
        </Button>
      )}
    </div>
  )
}
