import React from 'react'
import axios from 'axios'


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
        <div className="container">


          <div className="level">
            <div className="level-left">
              <h1 className="title is-1">{this.state.brewery.name}</h1>
            </div>

          </div>

          <div className="columns is-multiline">
            <div className="column is-half-desktop is-full-tablet">


              <figure className="image">
                <img src={this.state.brewery.image} alt={this.state.brewery.name} />
              </figure>
            </div>

            <div className="column is-half-desktop is-full-tablet">
              <h2 className="title is-2">{this.state.brewery.area}</h2>

              <hr />

              <h2 className="title is-2">{this.state.brewery.founded}</h2>


            </div>
          </div>
        </div>
      </section>
    )
  }
}
export default Show
