import React from 'react'
import axios from 'axios'


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
          <div className="level">
            <div className="level-left">
              <h1 className="title is-1">{this.state.style.name}</h1>
            </div>
          </div>
        </div>
      </section>
    )
  }
}
export default Show
