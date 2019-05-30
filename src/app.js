import React from 'react'
import ReactDOM from 'react-dom'
import { HashRouter as Router, Switch, Route } from 'react-router-dom'

import Home from './components/common/Home'
import Navbar from './components/common/Navbar'

import 'bulma'

class App extends React.Component {
  render(){
    return(
      <Router>
        <div>
          <Navbar />
          <Route path="/" component={Home} />
        </div>
      </Router>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
