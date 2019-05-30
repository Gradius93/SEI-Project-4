import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import Auth from '../../lib/Auth'

class Navbar extends React.Component {
  constructor(){
    super()
    this.state = {
      active: false
    }
    this.logout = this.logout.bind(this)
    this.toggleActive = this.toggleActive.bind(this)
  }
  logout(){
    Auth.removeToken()
    this.props.history.push('/')
  }
  toggleActive(){
    this.setState({ active: !this.state.active})
  }
  render() {
    return (
      <nav className="navbar is-fixed-top">
        <div className="navbar-brand">
          <Link to="/" className="navbarItem">Home/Logo</Link>

          <a role="button" className={`navbar-burger${this.state.active ? ' is-active' : ''}`}
            onClick={this.toggleActive}>

            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
        <div>

        </div>

        <div className={`navbar-menu${this.state.active ? ' is-active' : ''}`}>

          <div className="navbar-start">
            <Link to="/beers" className="navbar-item">Beers</Link>

          </div>

          <div className="navbar-end">
            {!Auth.isAuthenticated() &&<Link to="/register" className="navbar-item">Register</Link>}
            {!Auth.isAuthenticated() &&<Link to="/login" className="navbar-item">Login</Link>}
            {Auth.isAuthenticated() && <a className= "navbar-item" onClick={this.logout}>Logout</a>}
          </div>
        </div>
      </nav>
    )
  }
}

export default withRouter(Navbar)
