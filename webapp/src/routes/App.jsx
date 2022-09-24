import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import Layout from '../containers/Layout'
import AppContext from '../context/AppContext'
import useInitialState from '../hooks/useInitialState'
import Home from '@pages/Home'
import Member from "@pages/Member";
import Repository from "@pages/Repository";
import Organization from "@pages/Organization";
import NotFound from '@pages/NotFound'
import Login from '@pages/Login'
import '../scss/styles.scss'
import organization from "../pages/Organization";

const App = () => {
  const initialState = useInitialState()
  if (!initialState.state.user.id) {
    return (
      <AppContext.Provider value={initialState}>
        <Login />
      </AppContext.Provider>
    )
  }
  return (
    <AppContext.Provider value={initialState}>
      <BrowserRouter>
        <Layout>
          <Switch>
            <Route exact path='/' component={Home} />
            <Route path='/members' component={Member} />
            <Route path='/repositories' component={Repository} />
            <Route path='/organizations' component={Organization} />
            <Route path='*' component={NotFound} />
          </Switch>
        </Layout>
      </BrowserRouter>
    </AppContext.Provider>

  )
}

export default App
