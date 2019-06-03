import React from 'react'
import axios from 'axios'
import Card from './Card'
import { Link } from 'react-router-dom'

class Index extends React.Component {
  constructor() {
    super()

    this.state= {
      breweries: []
    }
  }

  componentDidMount() {
    axios('/api/breweries')
      .then(res => this.setState({ breweries: res.data }))
  }

  render() {
    if(!this.state.breweries) return null
    return (
      <section className="section">
        <div className="container pad">
          <div className="columns is-multiline">
            {this.state.breweries.map(brewery =>
              <div key={brewery.id} className="column is-one-fifth-desktop is-one-third-tablet">
                <Link to={`/breweries/${brewery.id}`}>
                  <Card {...brewery} />
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
