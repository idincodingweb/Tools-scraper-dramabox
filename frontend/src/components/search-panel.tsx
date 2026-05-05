import { useState } from 'react'
import { Search } from 'lucide-react'
import { Button } from './ui/button'
import { Card } from './ui/card'
import { Input } from './ui/input'

type Props = { onResult: (data: unknown) => void }

export function SearchPanel({ onResult }: Props) {
  const [keyword, setKeyword] = useState('')

  const doSearch = async () => {
    const res = await fetch('/api/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ keyword, page: 1, size: 20 }),
    })
    onResult(await res.json())
  }

  const doLatest = async () => {
    const res = await fetch('/api/latest', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ page: 1, size: 20 }),
    })
    onResult(await res.json())
  }

  return (
    <Card>
      <h2>Browse Drama</h2>
      <div className="row">
        <Input placeholder="Search keyword" value={keyword} onChange={(e) => setKeyword(e.target.value)} />
        <Button onClick={doSearch}><Search size={16} /> Search</Button>
        <Button variant="secondary" onClick={doLatest}>Latest</Button>
      </div>
    </Card>
  )
}
