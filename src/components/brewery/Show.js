import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import Card from '../beer/Card'

class Show extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      brewery: null
    }
  }

  componentDidMount() {
    axios.get(`/api/breweries/${this.props.match.params.id}`)
      .then(res => this.setState({ brewery: res.data }))
  }


  render() {
    if(!this.state.brewery) return null
    return(
      <section className="section">
        <div className="container pad">


          <div className="level">
            <div className="level-left">

            </div>

          </div>

          <div className="columns is-multiline">
            <div className="column is-half-desktop is-full-tablet">


              <figure className="image brew">
                <img src={this.state.brewery.image} alt={this.state.brewery.name} />
                <h1 className="title is-1 brew-text">{this.state.brewery.name}</h1>
              </figure>
            </div>

            <div className="column is-half-desktop is-full-tablet info">
              <h2 className="title is-2">{this.state.brewery.area} - est. {this.state.brewery.founded}</h2>

              <hr />

              <p> {this.state.brewery.info} </p>


            </div>
          </div>
          <div className="container">
            <div className="breweryBeers columns is-multiline">
              {this.state.brewery.beers.map(beer =>
                <div key={beer.id} className="column is-one-fifth">
                  <Link to={`/beers/${beer.id}`}>
                    <Card {...beer} />
                  </Link>
                </div>
              )}
            </div>
          </div>
        </div>
      </section>
    )
  }
}
export default Show
