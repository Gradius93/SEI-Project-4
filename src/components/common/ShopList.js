import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import { Link } from 'react-router-dom'

class ShopList extends React.Component {
  constructor() {
    super()

    this.state = {
      shopping_list: null
    }

    this.handleAdd = this.handleAdd.bind(this)
  }


  handleAdd() {
    axios.post(`/api/beers/${this.props.match.params.id}/list`, null, {
      headers: { 'Authorization': `Bearer ${Auth.getToken()}` }
    })
      .then(() => this.props.history.push('/users/'))
  }

  render() {
    return(
      <section className="section">
        <div className="container">
          <h3 className="subtitle subheading-show">Shopping List</h3>

          <div className="columns is-multiline">
            {this.state.user.shopping_list.map(beer =>
              <div key={beer.id} className="column is-one-quarter">
                <Link to={`/beers/${beer.id}`}>
                  <img src={beer.image} alt={beer.name} />
                </Link>
              </div>
            )}
          </div>
        </div>
      </section>
    )
  }
}

export default ShopList
