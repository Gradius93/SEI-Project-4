import React from 'react'
import { Link } from 'react-router-dom'

class Navbar extends React.Component {
  constructor(){
    super()
    this.state = {
      active: false
    }
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
            <Link to="/register" className="navbar-item">Register</Link>
            <Link to="/login" className="navbar-item">Login</Link>
          </div>
        </div>
      </nav>
    )
  }
}

export default Navbar
