import React from 'react'
import axios from 'axios'

class Register extends React.Component {

  constructor() {
    super()

    this.state = {
      data: {},
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange({target: { name, value }}) {
    const data = { ...this.state.data, [name]: value }
    const errors = { ...this.state.errors, [name]: '' }
    this.setState({ data, errors })
  }

  handleSubmit(e) {
    e.preventDefault()
    console.log(this.state.data)
    axios.post('/api/register', this.state.data)
      .then(() => this.props.history.push('/login'))
      .catch(err => this.setState({ errors: err.response.data.error }))
  }

  render() {
    console.log(this.state)
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
                        <label className="label">Username</label>
                        <div className="control">
                          <input
                            className="input"
                            name="username"
                            placeholder="eg: VinnieDaVinylHead45"
                            onChange={this.handleChange}
                          />
                        </div>
                      </div>
                      <div className="field">
                        <label className="label">Email</label>
                        <div className="control">
                          <input
                            className="input"
                            name="email"
                            placeholder="eg: VinnieDaVinyl@technics.com"
                            onChange={this.handleChange}
                          />
                        </div>
                        {this.state.errors.email && <div className="help is-danger">{this.state.errors.email}</div>}
                      </div>
                      <div className="field">
                        <label className="label">Password</label>
                        <div className="control">
                          <input
                            className="input"
                            name="password"
                            type="password"
                            placeholder="eg: ••••••••"
                            onChange={this.handleChange}
                          />
                        </div>
                        {this.state.errors.password && <div className="help is-danger">{this.state.errors.password}</div>}
                      </div>
                      <div className="field">
                        <label className="label">Password Confirmation</label>
                        <div className="control">
                          <input
                            className="input"
                            name="password_confirmation"
                            type="password"
                            placeholder="eg: ••••••••"
                            onChange={this.handleChange}
                          />
                        </div>
                        {this.state.errors.password_confirmation && <div className="help is-danger">{this.state.errors.passwordConfirmation}</div>}
                      </div>
                      {this.state.errors.password_confirmation && <div className="help is-danger">{this.state.errors.passwordConfirmation}</div>}
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

export default Register
