import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import Card from '../beer/Card'


class Show extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      style: null
    }
  }

  componentDidMount() {
    axios.get(`/api/styles/${this.props.match.params.id}`)
      .then(res => this.setState({ style: res.data }))
  }


  render() {
    if(!this.state.style) return null
    return(
      <section className="section">
        <div className="container">
          <h1 className="title brewsec is-1">{this.state.style.name}</h1>
          <div className="level">
            <div className="level-left">
            </div>
            <div className="level">
              <div className="info">
                <p>{this.state.style.info}</p>
              </div>
            </div>
          </div>
        </div>
        <div className="container">
          <div className="breweryBeers pad columns is-multiline">
            {this.state.style.beers.map(beer =>
              <div key={beer.id} className="column is-one-fifth">
                <Link to={`/beers/${beer.id}`}>
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
export default Show
