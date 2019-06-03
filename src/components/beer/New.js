import React from 'react'
import axios from 'axios'
import Select from 'react-select'
import Promise from 'bluebird'

import Auth from '../../lib/Auth'

class New extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      data: {},
      errors: null,
      beers: [],
      style: [],
      brewery: []
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleBrewerySelect = this.handleBrewerySelect.bind(this)
    this.handleStyleSelect = this.handleStyleSelect.bind(this)
  }

  getData() {
    Promise.props({
      style: axios.get('/api/styles').then(res => res.data),
      brewery: axios.get('/api/breweries').then(res => res.data)
    })
      .then(res => this.setState(res))
  }

  componentDidMount() {
    this.getData()
  }

  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    this.setState({ data })
    console.log(this.state)
  }

  handleBrewerySelect(e) {
    const data = { ...this.state.data, brewery_id: e.value }
    this.setState({ data })
  }

  handleStyleSelect(e) {
    const data = { ...this.state.data, style_id: e.value }
    this.setState({ data })
  }


  handleSubmit(e) {
    e.preventDefault()

    const token = Auth.getToken()

    axios.post('/api/beers', this.state.data, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/beers'))
      .catch(err => this.setState({ errors: err.response.data.errors }))

  }



  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns is-centered">
            <div className="column is-half-desktop is-two-thirds-tablet">
              <section className="section">
                <div className="container is-fluid">
                  <div className="formBox">
                    <form onSubmit={this.handleSubmit}>
                      <div className="field">
                        <label className="label">Beer name</label>
                        <div className="control">
                          <input
                            className="input"
                            name="name"
                            placeholder="eg: Beery McBeer"
                            onChange={this.handleChange}
                            value={this.state.data.name || ''}
                          />
                        </div>
                        {this.state.errors && this.state.errors.name && <div className="help is-danger">{this.state.errors.name}</div>}
                      </div>
                      <div className="field">
                        <label className="label">Brewery</label>
                        <div className="control">
                          <Select
                            className="brewery"
                            placeholder={'Select something'}
                            onChange={this.handleBrewerySelect}
                            options={this.state.brewery.map(brewery => {
                              return {
                                value: brewery.id,
                                label: brewery.name
                              }
                            })
                            }
                          />
                        </div>
                        {this.state.errors && this.state.errors.brewery && <div className="help is-danger">{this.state.errors.brewery}</div>}
                      </div>
                      <div className="field">
                        <label className="label">Image</label>
                        <div className="control">
                          <input
                            className="input"
                            name="image"
                            placeholder="eg: https://beers.com/image/beer"
                            onChange={this.handleChange}
                            value={this.state.data.image || ''}
                          />
                        </div>
                        {this.state.errors && this.state.errors.image && <div className="help is-danger">{this.state.errors.image}</div>}
                      </div>
                      <div className="field">
                        <label className="label">Style</label>
                        <div className="control">
                          <Select
                            className="style"
                            placeholder={'Select something'}
                            onChange={this.handleStyleSelect}

                            options={this.state.style.map(style => {
                              return {
                                value: style.id,
                                label: style.name
                              }
                            })
                            }
                          />
                        </div>
                        {this.state.errors && this.state.errors.style && <div className="help is-danger">{this.state.errors.style}</div>}
                      </div>
                      <div className="field">
                        <label className="label">Hops</label>
                        <div className="control">
                          <input
                            className="input"
                            name="hops"
                            placeholder="eg: Mosaic, Simcoe, etc.."
                            onChange={this.handleChange}
                            value={this.state.data.hops || ''}
                          />
                        </div>
                        {this.state.errors && this.state.errors.hops && <div className="help is-danger">{this.state.errors.hops}</div>}
                      </div>
                      <div className="field">
                        <label className="label">Region</label>
                        <div className="control">
                          <input
                            className="input"
                            name="region"
                            placeholder="eg: UK, USA, Europe, Australasia"
                            onChange={this.handleChange}
                            value={this.state.data.region || ''}
                          />
                        </div>
                        {this.state.errors && this.state.errors.region && <div className="help is-danger">{this.state.errors.region}</div>}
                      </div>
                      <div className="field">
                        <label className="label">ABV (%)</label>
                        <div className="control">
                          <input
                            className="input"
                            name="abv"
                            placeholder="eg: 4.2"
                            onChange={this.handleChange}
                            value={this.state.data.abv || ''}
                          />
                        </div>
                        {this.state.errors && this.state.errors.abv && <div className="help is-danger">{this.state.errors.abv}</div>}
                      </div>
                      <div className="field">
                        <label className="label">Price (£)</label>
                        <div className="control">
                          <input
                            className="input"
                            name="price"
                            type="number"
                            placeholder="eg: 3.49"
                            onChange={this.handleChange}
                            value={this.state.data.price || ''}
                          />
                        </div>
                        {this.state.errors && this.state.errors.price && <div className="help is-danger">{this.state.errors.price}</div>}
                      </div>
                      <div className="field">
                        <label className="label">Tasty Notes</label>
                        <div className="control">
                          <input
                            className="textarea"
                            name="tasting_notes"
                            placeholder="eg: Citrusy, Hoppy, Spiky..."
                            onChange={this.handleChange}
                            value={this.state.data.tasting_notes || ''}
                          />
                        </div>
                        {this.state.errors && this.state.errors.tasting_notes && <div className="help is-danger">{this.state.errors.tasting_notes}</div>}
                      </div>
                      <button className="button is-dark">Submit</button>
                    </form>
                  </div>
                </div>
              </section>
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default New
