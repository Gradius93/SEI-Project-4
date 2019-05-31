import React from 'react'
import ReactDOM from 'react-dom'
import { HashRouter as Router, Switch, Route } from 'react-router-dom'

import Home from './components/common/Home'
import Navbar from './components/common/Navbar'

import BeerIndex from './components/beer/Index'
import BeerShow from './components/beer/Show'

import BreweryIndex from './components/brewery/Index'
import BreweryShow from './components/brewery/Show'

import StyleIndex from './components/style/Index'
import StyleShow from './components/style/Show'

import Login from './components/auth/Login'
import Register from './components/auth/Register'

import 'bulma'

class App extends React.Component {
  render() {
    return(
      <Router>
        <div>
          <Navbar />
          <Switch>
            <Route path="/styles/:id" component={StyleShow} />
            <Route path="/styles" component={StyleIndex} />

            <Route path="/breweries/:id" component={BreweryShow} />
            <Route path="/breweries" component={BreweryIndex} />

            <Route path="/beers/:id" component={BeerShow} />
            <Route path="/beers" component={BeerIndex} />

            <Route path="/register" component={Register} />
            <Route path="/login" component={Login} />
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
