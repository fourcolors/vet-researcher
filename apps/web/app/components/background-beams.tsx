import { cn } from "~/lib/utils"

export const BackgroundBeams = ({ className }: { className?: string }) => {
  return (
    <div className={cn("h-full w-full absolute inset-0", className)}>
      <div className="absolute inset-0 bg-gradient-to-b from-gray-50 to-gray-200 [mask-image:radial-gradient(ellipse_at_center,transparent_20%,black)]" />
      <div className="absolute inset-0 overflow-hidden">
        <div className="h-full w-full relative">
          {/* Beam 1 */}
          <div
            className="absolute top-0 -left-1/4 w-1/2 h-full
              rotate-[25deg] transform-gpu bg-gradient-to-r from-transparent via-blue-100 to-transparent 
              blur-[100px] opacity-50"
            style={{
              animation: "beam-move 10s infinite linear",
            }}
          />
          {/* Beam 2 */}
          <div
            className="absolute top-0 -right-1/4 w-1/2 h-full
              -rotate-[25deg] transform-gpu bg-gradient-to-r from-transparent via-blue-200 to-transparent 
              blur-[100px] opacity-50"
            style={{
              animation: "beam-move 15s infinite linear",
            }}
          />
        </div>
      </div>
    </div>
  )
}

