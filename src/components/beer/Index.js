import React from 'react'
import axios from 'axios'
import Card from './Card'

class Index extends React.Component {
  constructor(props) {
    super(props)

    this.state= {
      beers: []
    }
  }

  componentDidMount() {
    axios('/api/beers')
      .then(res => this.setState({ beers: res.data }))
  }

  render() {
    if(!this.state.vinyls) return null
    return (
      <section className="section">
        <div className="container">
          <div className="columns is-multiline">
            {this.state.beers.map(beer =>
              <div key={beer._id} className="column is-one-quarter-desktop is-one-third-tablet">
                <Card {...beer} />
              </div>
            )}
          </div>
        </div>
      </section>
    )
  }
}
export default Index
