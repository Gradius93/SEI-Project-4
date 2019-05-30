import React from 'react'
import axios from 'axios'


class Show extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      beer: null,
      brewery: null
    }
  }

  componentDidMount() {
    axios.get(`/api/beers/${this.props.match.params.id}`)
      .then(res => this.setState({ beer: res.data }))
  }


  render() {
    if(!this.state.beer) return null
    return(
      <section className="section">
        <div className="container">


          <div className="level">
            <div className="level-left">
              <h1 className="title is-1">{this.state.beer.name}</h1>
            </div>

          </div>

          <div className="columns is-multiline">
            <div className="column is-half-desktop is-full-tablet">


              <figure className="image">
                <img src={this.state.beer.image} alt={this.state.beer.name} />
              </figure>
            </div>

            <div className="column is-half-desktop is-full-tablet">
              <div className="level-left">
                <h1 className="title is-1">{this.state.beer.name}</h1>
              </div>
              <h2 className="title is-2">{this.state.beer.region}</h2>

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
