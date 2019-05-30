import React from 'react'
import ReactDOM from 'react-dom'
import { HashRouter as Router, Switch, Route } from 'react-router-dom'

import Home from './components/common/Home'
import Navbar from './components/common/Navbar'

import BeerIndex from './components/beer/Index'

import Login from './components/auth/Login'
import Register from './components/auth/Register'

import 'bulma'

class App extends React.Component {
  render(){
    return(
      <Router>
        <div>
          <Navbar />
          <Switch>
            <Route path="/register" component={Register} />
            <Route path="/login" component={Login} />
            <Route path="/beers" component={BeerIndex} />
            <Route path="/" component={Home} />
          </Switch>
        </div>
      </Router>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
