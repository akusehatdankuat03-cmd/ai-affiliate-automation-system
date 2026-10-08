const products = [
  {
    title: 'Portable Blender',
    category: 'Kitchen & Daily Use',
    affiliate: true,
    score: 88,
    source: 'China Market',
  },
  {
    title: 'Mini Desk Fan',
    category: 'Lifestyle',
    affiliate: false,
    score: 76,
    source: 'TikTok Trend',
  },
  {
    title: 'Smart Electric Toothbrush',
    category: 'Beauty',
    affiliate: true,
    score: 91,
    source: 'Shopee Trend',
  },
]

export default function App() {
  return (
    <main style={{ padding: 32, fontFamily: 'Arial, sans-serif', background: '#f5f7fb', minHeight: '100vh' }}>
      <h1>AI Affiliate Automation Dashboard</h1>
      <p style={{ color: '#4b5563' }}>Human-in-the-loop approval workflow for product research and publishing.</p>

      <section style={{ display: 'grid', gap: 16, gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', marginTop: 24 }}>
        <Card title="Products Found" value="24" color="#2563eb" />
        <Card title="Affiliate Valid" value="15" color="#16a34a" />
        <Card title="Approved" value="7" color="#a16207" />
        <Card title="Published" value="3" color="#7c3aed" />
      </section>

      <section style={{ marginTop: 32 }}>
        <h2>Shortlist</h2>
        <table style={{ width: '100%', background: '#fff', borderRadius: 12, overflow: 'hidden', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ background: '#e2e8f0' }}>
              <th style={{ padding: 12, textAlign: 'left' }}>Product</th>
              <th>Category</th>
              <th>Affiliate</th>
              <th>Score</th>
              <th>Source</th>
            </tr>
          </thead>
          <tbody>
            {products.map((p) => (
              <tr key={p.title} style={{ borderTop: '1px solid #e5e7eb' }}>
                <td style={{ padding: 12 }}>{p.title}</td>
                <td>{p.category}</td>
                <td>{p.affiliate ? 'Yes' : 'No'}</td>
                <td>{p.score}</td>
                <td>{p.source}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </main>
  )
}

function Card({ title, value, color }) {
  return (
    <div style={{ background: '#fff', borderRadius: 12, padding: 20, boxShadow: '0 4px 12px rgba(0,0,0,0.06)' }}>
      <div style={{ fontSize: 13, color: '#6b7280' }}>{title}</div>
      <div style={{ fontSize: 32, fontWeight: 700, color }}>{value}</div>
    </div>
  )
}
