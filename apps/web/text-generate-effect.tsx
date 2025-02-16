import { useEffect } from "react"
import { motion, stagger, useAnimate } from "framer-motion"

export const TextGenerateEffect = ({
  words,
  className = "",
}: {
  words: string
  className?: string
}) => {
  const [scope, animate] = useAnimate()

  useEffect(() => {
    animate(
      "span",
      {
        opacity: 1,
      },
      {
        duration: 2,
        delay: stagger(0.2),
      },
    )
  }, [animate])

  const wordsArray = words.split(" ")

  return (
    <motion.div ref={scope} className={className}>
      {wordsArray.map((word, i) => (
        <motion.span key={i} className="inline-block mr-1">
          {word.split("").map((char, charIndex) => (
            <motion.span initial={{ opacity: 0 }} key={`${i}-${charIndex}`} className="inline-block">
              {char}
            </motion.span>
          ))}
        </motion.span>
      ))}
    </motion.div>
  )
}

