"use client"

import { cn } from "~/lib/utils"
import type React from "react"

export const BackgroundGradient = ({
  children,
  className,
}: {
  children: React.ReactNode
  className?: string
}) => {
  return (
    <div className={cn("relative group/card  w-full", className)}>
      <div className="absolute -inset-px bg-gradient-to-r from-purple-500 to-pink-500 rounded-lg blur opacity-25 group-hover/card:opacity-75 transition duration-1000"></div>
      <div className={cn("relative", className)}>{children}</div>
    </div>
  )
}

