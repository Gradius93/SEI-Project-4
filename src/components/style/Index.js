import React from 'react'
import axios from 'axios'
import Card from './Card'
import { Link } from 'react-router-dom'

class Index extends React.Component {
  constructor() {
    super()

    this.state= {
      styles: []
    }
  }

  componentDidMount() {
    axios('/api/styles')
      .then(res => this.setState({ styles: res.data }))
  }

  render() {
    if(!this.state.styles) return null
    return (
      <section className="section">
        <div className="container">
          <div className="columns is-multiline">
            {this.state.styles.map(style =>
              <div key={style.id} className="column is-one-fifth-desktop is-one-third-tablet">
                <Link to={`/styles/${style.id}`}>
                  <Card {...style} />
                </Link>
              </div>
            )}
          </div>
        </div>
      </section>
    )
  }
}
export default Index
