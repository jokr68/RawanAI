import type { Metadata, Viewport } from 'next'
import { IBM_Plex_Sans_Arabic, Geist_Mono } from 'next/font/google'
import { Analytics } from '@vercel/analytics/next'
import './globals.css'

const _ibmPlex = IBM_Plex_Sans_Arabic({
  subsets: ['arabic', 'latin'],
  weight: ['300', '400', '500', '600', '700'],
})
const _geistMono = Geist_Mono({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'RawanAI - وكيلة الذكاء الاصطناعي الشخصية',
  description:
    'روان، وكيلة ذكاء اصطناعي شخصية بلهجة سودانية جداوية للمساعدة اليومية وتحليل العادات وتطوير الذات',
  generator: 'v0.app',
  keywords: ['AI', 'assistant', 'Arabic', 'habits', 'analytics', 'RawanAI'],
  authors: [{ name: 'Ahmed Al-Dosari' }],
  openGraph: {
    title: 'RawanAI - وكيلة الذكاء الاصطناعي الشخصية',
    description: 'وكيلة ذكاء اصطناعي شخصية بشخصية عربية أصيلة',
    type: 'website',
    locale: 'ar_SA',
  },
}

export const viewport: Viewport = {
  themeColor: '#0a0a12',
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="ar" dir="rtl" className="dark">
      <body className="font-sans antialiased">
        {children}
        <Analytics />
      </body>
    </html>
  )
}
