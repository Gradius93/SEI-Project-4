import React from 'react'
import axios from 'axios'
import Promise from 'bluebird'


class Show extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      beer: null,
      brewery: null
    }
  }

  getData() {
    Promise.props({
      beer: axios.get(`/api/beers/${this.props.match.params.id}`).then(res => this.setState({ beer: res.data })),
      brewery: axios.get(`/api/breweries/${this.props.match.params.id}`).then(res => this.setState({ brewery: res.data }))
    })
  }
  componentDidMount() {
    this.getData()
  }


  render() {
    if(!this.state.beer) return null
    return(
      <section className="section">
        <div className="container pad">




          <div className="columns is-multiline">
            <div className="column is-half-desktop is-full-tablet">


              <figure className="image">
                <img src={this.state.beer.image} alt={this.state.beer.name} />
              </figure>
            </div>

            <div className="column info is-half-desktop is-full-tablet">
              <div className="level-left">
                <h1 className="title is-1 level-right">{this.state.beer.name}</h1>
              </div>
              <div className="level-left">
                <h3 className="subtitle is-3">{this.state.beer.brewery.name}
                </h3>
                <hr />
              </div>
              <div className="level-left">
                <h3 className="subtitle is-3">{this.state.beer.region}  •  {this.state.beer.abv}%  •  £{this.state.beer.price}</h3>
              </div>
              <hr />

              <p>{this.state.beer.tasting_notes}</p>

            </div>
          </div>
        </div>
      </section>
    )
  }
}
export default Show
