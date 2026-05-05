import { ButtonHTMLAttributes } from 'react'
import { cn } from '../../lib'

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: 'default' | 'secondary'
}

export function Button({ className, variant = 'default', ...props }: ButtonProps) {
  return (
    <button
      className={cn(
        'btn',
        variant === 'default' ? 'btn-default' : 'btn-secondary',
        className,
      )}
      {...props}
    />
  )
}
