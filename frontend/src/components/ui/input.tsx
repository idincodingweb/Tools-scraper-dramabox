import { InputHTMLAttributes } from 'react'
import { cn } from '../../lib'

export function Input({ className, ...props }: InputHTMLAttributes<HTMLInputElement>) {
  return <input className={cn('input', className)} {...props} />
}
