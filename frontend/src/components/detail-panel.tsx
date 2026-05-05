import { useState } from 'react'
import { Button } from './ui/button'
import { Card } from './ui/card'
import { Input } from './ui/input'

type Props = { onResult: (data: unknown) => void }

export function DetailPanel({ onResult }: Props) {
  const [dramaId, setDramaId] = useState('')

  const getDetail = async () => {
    const res = await fetch(`/api/detail/${dramaId}`)
    onResult(await res.json())
  }

  const getEpisodes = async () => {
    const res = await fetch(`/api/episodes/${dramaId}?page=1&size=100`)
    onResult(await res.json())
  }

  return (
    <Card>
      <h2>Detail & Episodes</h2>
      <div className="row">
        <Input placeholder="Drama ID" value={dramaId} onChange={(e) => setDramaId(e.target.value)} />
        <Button onClick={getDetail}>Detail</Button>
        <Button variant="secondary" onClick={getEpisodes}>Episodes</Button>
      </div>
    </Card>
  )
}
