



1. Install react-router-dom
   `npm i react-router-dom`

2. Update App.js

   - Add Router and create Routes
     HashRouter is used to avoid server side routing.

   ```react
   import React, { Component, Fragment } from 'react'
   import ReactDOM from 'react-dom'
   
   import { Provider } from 'react-redux'
   import store from '../store'
   import Dashboard from './watchlists/Dashboard'
   
   import { HashRouter as Router, Switch, Route, Redirect } from 'react-router-dom'
   import Login from './watchlists/accounts/Login'
   import Register from './watchlists/accounts/Register'
   import Header from './watchlists/layout/Header'
   
   class App extends Component {
   	render() {
   		return (
   			<Provider store={store}>
   				<Router>
   					<Fragment>
                           <Header />
                           <div className="container">
                               <Switch>
                                   <Route path="/" exact component={Dashboard} />
                                   <Route path="/login" exact component={Login} />
                                   <Route path="/register" exact component={Register} />
                               </Switch>
                           </div>
   					</Fragment>
   				</Router>
   			</Provider>
   		)
   	}
   }
   
   ReactDOM.render(<App />, document.getElementById('app'))
   ```

3. Create Register and Login pages/components.

   Register.js

   ```react
   import React, { Fragment, useState } from 'react'
   import { Link } from 'react-router-dom'
   
   const Register = () => {
   	const initialState = {
   		username: '',
   		password: '',
   		email: '',
   		password2: ''
   	}
   
   	const [ userInfo, setUserInfo ] = useState(initialState)
   
   	const onChange = (event) => {
   		setUserInfo({ ...userInfo, [event.target.name]: event.target.value })
   	}
   
   	const onSubmit = (event) => {
   		event.preventDefault()
   		console.log('submit')
   	}
   
   	return (
   		<Fragment>
               <div className="row">
                   <div className="col-lg-10 col-xl-9 mx-auto">
                       <div className="card card-signin flex-row my-5">
                           <div className="card-img-left d-none d-md-flex" />
                           <div className="card-body">
                               <h5 className="card-title text-center">Register</h5>
                               <form className="form-signin">
                                   <div className="form-label-group">
                                       <input
                                           type="text"
                                           id="inputUserame"
                                           className="form-control"
                                           placeholder="Username"
                                           required
                                           autoFocus
                                           name="username"
                                           value={userInfo.username}
                                           onChange={onChange}
                                       />
                                       <label htmlFor="inputUserame">Username</label>
                                   </div>
   
                                   <div className="form-label-group">
                                       <input
                                           type="email"
                                           id="inputEmail"
                                           className="form-control"
                                           placeholder="Email address"
                                           required
                                           name="email"
                                           value={userInfo.email}
                                           onChange={onChange}
                                       />
                                       <label htmlFor="inputEmail">Email address</label>
                                   </div>
   
                                   <hr />
   
                                   <div className="form-label-group">
                                       <input
                                           type="password"
                                           id="inputPassword"
                                           className="form-control"
                                           placeholder="Password"
                                           required
                                           name="password"
                                           value={userInfo.password}
                                           onChange={onChange}
                                       />
                                       <label htmlFor="inputPassword">Password</label>
                                   </div>
   
                                   <div className="form-label-group">
                                       <input
                                           type="password"
                                           id="inputConfirmPassword"
                                           className="form-control"
                                           placeholder="Confirm Password"
                                           required
                                           name="password2"
                                           value={userInfo.password2}
                                           onChange={onChange}
                                       />
                                       <label htmlFor="inputConfirmPassword">Confirm password</label>
                                   </div>
   
                                   <button className="btn btn-lg btn-primary btn-block text-uppercase" type="submit">
                                       Register
                                   </button>
                                   <p>
                                       Already have an account?
                                       <Link to="/login">Login</Link>
                                   </p>
                               </form>
                           </div>
                       </div>
                   </div>
               </div>
   		</Fragment>
   	)
   }
   
   export default Register
   ```

   

   Login.js

   ```react
   import React, { Fragment, useState } from 'react'
   import { Link } from 'react-router-dom'
   
   const Login = () => {
   	const initialState = {
   		username: '',
   		password: ''
   	}
   
   	const [ userInfo, setUserInfo ] = useState(initialState)
   
   	const onChange = (event) => {
   		setUserInfo({ ...userInfo, [event.target.name]: event.target.value })
   	}
   
   	const onSubmit = (event) => {
   		event.preventDefault()
   		console.log('submit')
   	}
   
   	return (
   		<Fragment>
               <div className="row">
                   <div className="col-sm-9 col-md-7 col-lg-5 mx-auto">
                       <div className="card card-signin my-5">
                           <div className="card-body">
                               <h5 className="card-title text-center">Sign In</h5>
                               <form className="form-signin" onSubmit={onSubmit}>
                                   <div className="form-label-group">
                                       <input
                                           type="text"
                                           id="inputEmail"
                                           className="form-control"
                                           placeholder="Username"
                                           required
                                           autoFocus
                                           name="username"
                                           value={userInfo.username}
                                           onChange={onChange}
                                       />
                                       <label htmlFor="inputEmail">Email address</label>
                                   </div>
   
                                   <div className="form-label-group">
                                       <input
                                           type="password"
                                           id="inputPassword"
                                           className="form-control"
                                           placeholder="Password"
                                           required
                                           name="password"
                                           value={userInfo.password}
                                           onChange={onChange}
                                       />
                                       <label htmlFor="inputPassword">Password</label>
                                   </div>
   
                                   <div className="custom-control custom-checkbox mb-3">
                                       <input type="checkbox" className="custom-control-input" id="customCheck1" />
                                       <label className="custom-control-label" htmlFor="customCheck1">
                                           Remember password
                                       </label>
                                   </div>
                                   <button className="btn btn-lg btn-primary btn-block text-uppercase" type="submit">
                                       Sign in
                                   </button>
                                   <p>
                                       Don't have an account?
                                       <Link to="/register">Register</Link>
                                   </p>
                               </form>
                           </div>
                       </div>
                   </div>
               </div>
   		</Fragment>
   	)
   }
   
   export default Login
   ```

4. Update navbar Header.js
   Header.js

   ```react
   import React, { Component } from 'react'
   import { Link } from 'react-router-dom'
   
   export class Header extends Component {
   	render() {
   		return (
   			<nav className="navbar navbar-expand-sm navbar-light bg-light">
   				<div className="container">
   					<button
   						className="navbar-toggler"
   						type="button"
   						data-toggle="collapse"
   						data-target="#navbarTogglerDemo01"
   						aria-controls="navbarTogglerDemo01"
   						aria-expanded="false"
   						aria-label="Toggle navigation"
   					>
   						<span className="navbar-toggler-icon" />
   					</button>
   					<div className="collapse navbar-collapse" id="navbarTogglerDemo01">
   						<Link className="navbar-brand" to="/">
   							Portfolio Manager
   						</Link>
   					</div>
   					<ul className="navbar-nav ml-auto mt-2 mt-lg-0">
   						<li className="nav-item">
   							<Link to="/register" className="nav-link">
   								Register
   							</Link>
   						</li>
   						<li className="nav-item">
   							<Link to="/login" className="nav-link">
   								Login
   							</Link>
   						</li>
   					</ul>
   				</div>
   			</nav>
   		)
   	}
   }
   
   export default Header
   ```

5. Create an auth reducer to store authentication state.
   reducers/auth.js

   ```react
   import { USER_LOADED, USER_LOADING, AUTH_ERROR } from '../actions/types'
   
   const initialState = {
   	token: localStorage.getItem('token'),
   	isAuthenticated: null,
   	isLoading: false,
   	user: null
   }
   
   export default function(state = initialState, action) {
   	switch (action.type) {
   		default:
   			return state
   	}
   }
   ```

6. Update index reducer.
   reducers/index.js

   ```react
   import { combineReducers } from 'redux'
   import watchlists from './watchlists'
   import watchlist_stocks from './watchlist_stocks'
   import edit_watchlist from './edit_watchlist'
   import auth from './auth'
   
   export default combineReducers({
   	watchlists,
   	watchlist_stocks,
   	edit_watchlist,
   	auth
   })
   ```

7. Create a PrivateRoute - Route which will check authentication before rendering the components.

   - This is a Higher Order Component which uses Route and takes Component/s as parameter/props.
   - Private Route will check if the "isAuthenticated" state is true, if it is only then it will render the component(Dashboard here).

   PrivateRoute.js

   ```react
   import React from 'react'
   import { connect } from 'react-redux'
   import { Route, Redirect } from 'react-router'
   
   const PrivateRoute = ({ component: Component, auth, ...rest }) => (
   	<Route
   		{...rest}
   		render={(props) => {
   			if (auth.isLoading) {
   				// you can add spinner here
   				return <h2>Loading...</h2>
   			} else if (!auth.isAuthenticated) {
   				return <Redirect to="/login" />
   			} else {
   				return <Component {...props} />
   			}
   		}}
   	/>
   )
   
   const mapStateToProps = (state) => ({
   	auth: state.auth
   })
   
   export default connect(mapStateToProps)(PrivateRoute)
   ```

   Update App.js to use PrivateRoute.
   App.js

   ```react
   import React, { Component, Fragment } from 'react'
   import ReactDOM from 'react-dom'
   
   import { Provider } from 'react-redux'
   import store from '../store'
   import Dashboard from './watchlists/Dashboard'
   
   import { HashRouter as Router, Switch, Route, Redirect } from 'react-router-dom'
   import Login from './watchlists/accounts/Login'
   import Register from './watchlists/accounts/Register'
   import Header from './watchlists/layout/Header'
   import PrivateRoute from './watchlists/common/PrivateRoute'
   
   class App extends Component {
   	render() {
   		return (
   			<Provider store={store}>
   				<Router>
   					<Fragment>
   						<Header />
                               <div className="container">
                                   <Switch>
                                       <PrivateRoute path="/" exact component={Dashboard} />
                                       <Route path="/login" exact component={Login} />
                                       <Route path="/register" exact component={Register} />
                                   </Switch>
                               </div>
   					</Fragment>
   				</Router>
   			</Provider>
   		)
   	}
   }
   
   ReactDOM.render(<App />, document.getElementById('app'))
   ```

8. Now, each component will check for authentication using token. 
   To facilitate that, auth actions need to be created and reducers for the same.


   actions/types.js

   ```react
   export const GET_WATCHLISTS = 'GET_WATCHLISTS'
   export const DELETE_WATCHLIST = 'DELETE_WATCHLIST'
   export const ADD_WATCHLIST = 'ADD_WATCHLIST'
   export const GET_STOCKS = 'GET_STOCKS'
   export const DELETE_STOCK = 'DELETE_STOCK'
   export const ADD_STOCK = 'ADD_STOCK'
   export const SHOW_POPUP = 'SHOW_POPUP'
   export const GET_COMPANIES_DETAILS = 'GET_COMPANIES_DETAILS'
   export const GET_WATCHLIST_FOR_EDIT = 'GET_WATCHLIST_FOR_EDIT'
   export const SHOW_EDIT_WATCHLIST_POPUP = 'SHOW_EDIT_WATCHLIST_POPUP'
   // Add following types
   export const USER_LOADING = 'USER_LOADING'
   export const USER_LOADED = 'USER_LOADED'
   export const AUTH_ERROR = 'AUTH_ERROR'
   ```

   actions/auth.js

   ```react
   import axios from 'axios'
   
   import { USER_LOADED, USER_LOADING, AUTH_ERROR } from './types'
   
   // CHECK TOKEN AND LOAD USER
   export const loadUser = () => (dispatch, getState) => {
   	// User Loading
   	dispatch({ type: USER_LOADING })
   
   	// Get token from state
   	const token = getState().auth.token
   
       // Headers
   	const config = {
   		headers: {
   			'Content-Type': 'application/json'
   		}
   	}
   
   	//  If token, add to headers config
   	if (token) {
   		config.headers['Authorization'] = `Token ${token}`
   	}
   
   	axios.get('/api/auth/user', config)
   		.then((res) => {
   			dispatch({
   				type: USER_LOADED,
   				payload: res.data
   			})
   		})
   		.catch((err) => {
           	 // add error handling for alert/toast here
   
   			dispatch({ type: AUTH_ERROR })
   		})
   }
   ```

   reducers/auth.js

   ```react
   import { USER_LOADED, USER_LOADING, AUTH_ERROR } from '../actions/types'
   
   const initialState = {
   	token: localStorage.getItem('token'),
   	isAuthenticated: null,
   	isLoading: false,
   	user: null
   }
   
   export default function(state = initialState, action) {
   	switch (action.type) {
   		case USER_LOADING:
   			return {
   				...state,
   				isLoading: true
   			}
   		case USER_LOADED:
   			return {
   				...state,
   				isAuthenticated: true,
   				isLoading: false,
   				user: action.payload
   			}
   		case AUTH_ERROR:
   			localStorage.removeItem('token')
   			return {
   				...state,
   				token: null,
   				user: null,
   				isAuthenticated: false,
   				isLoading: false
   			}
   		default:
   			return state
   	}
   }
   ```

9. To call the loadUser for all components, add it in App.js

   - The loadUser action is dispatched by store after the App component, which is a main component, is mounted.
   - This action will 
     - get the token from state 
     - check for user's authentication
     - and then set the state for authentication success or fail
   - This state data will be used by all the child components to verify authentication.

   App.js

   ```react
   import React, { Component, Fragment } from 'react'
   import ReactDOM from 'react-dom'
   
   import { Provider } from 'react-redux'
   import store from '../store'
   import Dashboard from './watchlists/Dashboard'
   
   import { HashRouter as Router, Switch, Route, Redirect } from 'react-router-dom'
   import Login from './watchlists/accounts/Login'
   import Register from './watchlists/accounts/Register'
   import Header from './watchlists/layout/Header'
   import PrivateRoute from './watchlists/common/PrivateRoute'
   import { loadUser } from '../actions/auth'
   
   class App extends Component {
       // call the loadUser here
   	componentDidMount() {
   		store.dispatch(loadUser())
   	}
   
   	render() {
   		return (
   			<Provider store={store}>
   				<Router>
   					<Fragment>
   						<Header />
                                   <div className="container">
                                       <Switch>
                                           <PrivateRoute path="/" exact component={Dashboard} />
                                           <Route path="/login" exact component={Login} />
                                           <Route path="/register" exact component={Register} />
                                       </Switch>
                                   </div>
   					</Fragment>
   				</Router>
   			</Provider>
   		)
   	}
}
   
   ReactDOM.render(<App />, document.getElementById('app'))
   ```
   
   

