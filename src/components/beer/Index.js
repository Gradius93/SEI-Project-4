import React from 'react'
import axios from 'axios'
import Card from './Card'
import { Link } from 'react-router-dom'

class Index extends React.Component {
  constructor() {
    super()

    this.state= {
      beers: []
    }
  }

  componentDidMount() {
    axios('/api/beers')
      .then(res => this.setState({ beers: res.data }))
  }

  render() {
    if(!this.state.beers) return null
    return (
      <section className="section">
        <div className="container">
          <div className="columns is-multiline">
            {this.state.beers.map(beer =>
              <div key={beer._id} className="column is-one-fifth-desktop is-one-third-tablet">
                <Link to={`/beers/${beer._id}`}>
                  <Card {...beer} />
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
