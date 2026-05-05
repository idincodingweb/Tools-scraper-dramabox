import { useState } from 'react'
import { DetailPanel } from './components/detail-panel'
import { SearchPanel } from './components/search-panel'
import { Card } from './components/ui/card'

export function App() {
  const [result, setResult] = useState<unknown>({ status: 'Ready' })

  return (
    <main className="container">
      <header>
        <h1>DramaBox Scraper Dashboard</h1>
        <p>React modular frontend with shadcn-style components.</p>
      </header>
      <SearchPanel onResult={setResult} />
      <DetailPanel onResult={setResult} />
      <Card>
        <h2>Response</h2>
        <pre>{JSON.stringify(result, null, 2)}</pre>
      </Card>
    </main>
  )
}
