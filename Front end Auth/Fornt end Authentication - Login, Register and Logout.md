



1. Add types for Login functionality.
   actions/types.js

   ```react
   export const LOGIN_SUCCESS = 'LOGIN_SUCCESS'
   export const LOGIN_FAIL = 'LOGIN_FAIL'
   ```

2. Add action for Login.
   actions/auth.js

   ```react
   // LOGIN USER
   export const login = (username, password) => (dispatch) => {
   	const config = {
   		headers: {
   			'Content-type': 'application/json'
   		}
   	}
   
   	// Request Body
   	const body = JSON.stringify({ username, password })
   
   	axios
   		.post('/api/auth/login', body, config)
   		.then((res) => {
   			dispatch({
   				type: LOGIN_SUCCESS,
   				payload: res.data
   			})
   		})
   		.catch((err) => {
   			// add error handling dispatch here
   
   			dispatch({ type: LOGIN_FAIL })
   		})
   }
   ```

3. Handle the actions in the reducer for the login action types.
   reducers/auth.js

   ```react
   import {
   	USER_LOADED,
   	USER_LOADING,
   	AUTH_ERROR,
   	LOGIN_FAIL,
   	LOGIN_SUCCESS
   } from '../actions/types'
   
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
   		case LOGIN_SUCCESS:
   			localStorage.setItem('token', action.payload.token)
   			return {
   				...state,
   				...action.payload,
   				isAuthenticated: true,
   				isLoading: false
   			}
   		case AUTH_ERROR:
   		case LOGIN_FAIL:
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

4. Call the login action in the Login component.
   Login.js

   ```react
   import React, { Fragment, useState } from 'react'
   import { Link, Redirect } from 'react-router-dom'
   import { connect } from 'react-redux'
   import { login } from '../../../actions/auth'
   
   const Login = ({ login, isAuthenticated }) => {
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
   		login(userInfo.username, userInfo.password)
   	}
   
       // if already logged in redirect to dashboard
   	if (isAuthenticated) {
   		return <Redirect to="/" />
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
   
   const mapStateToProps = (state) => ({
   	isAuthenticated: state.auth.isAuthenticated
   })
   
   export default connect(mapStateToProps, { login })(Login)
   ```

5. Add action type.
   actions/types.js

   ```react
   export const LOGOUT_SUCCESS = 'LOGOUT_SUCCESS'
   ```

6. Define action for logout.
   actions/auth.js

   ```react
   // LOGOUT USER
   export const logout = () => (dispatch, getState) => {
       // Get token from state
   	const token = getState().auth.token
   
   	const config = {
   		headers: {
   			'Content-Type': 'application/json'
   		}
   	}
   
   	//  If token, add to headers config
   	if (token) {
   		config.headers['Authorization'] = `Token ${token}`
   	}
       
   	axios
   		.post('/api/auth/logout', null, config)
   		.then((res) => {
   			dispatch({
   				type: LOGOUT_SUCCESS
   			})
   		})
   		.catch((err) => {
   			// add error handling dispatch here
   			console.log(err)
   		})
   }
   ```

7. Handle this action in the reducer.
   reducers/auth.js

   ```react
   import {
   	USER_LOADED,
   	USER_LOADING,
   	AUTH_ERROR,
   	LOGIN_FAIL,
   	LOGIN_SUCCESS,
   	LOGOUT_SUCCESS
   } from '../actions/types'
   
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
   		case LOGIN_SUCCESS:
   			localStorage.setItem('token', action.payload.token)
   			return {
   				...state,
   				...action.payload,
   				isAuthenticated: true,
   				isLoading: false
   			}
   		case AUTH_ERROR:
   		case LOGIN_FAIL:
   		case LOGOUT_SUCCESS:
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

   

8. Change the navbar to add Logout button.

   Header.js

   ```react
   import React, { Component } from 'react'
   import { Link } from 'react-router-dom'
   import { connect } from 'react-redux'
   import { logout } from '../../../actions/auth'
   
   const Header = ({ auth: { isAuthenticated, user }, logout }) => {
   	const authLinks = (
   		<ul className="navbar-nav ml-auto mt-2 mt-lg-0">
   			<span className="navbar-text mr-3">
   				<strong>{user ? `Welcome ${user.username}` : ''}</strong>
   			</span>
   			<li className="nav-item">
   				<button onClick={logout} className="nav-link btn btn-info btn-sm text-light">
   					Logout
   				</button>
   			</li>
   		</ul>
   	)
   
   	const guestLinks = (
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
   	)
   
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
   				{isAuthenticated ? authLinks : guestLinks}
   			</div>
   		</nav>
   	)
   }
   
   const mapStateToProps = (state) => ({
   	auth: state.auth
   })
   
   export default connect(mapStateToProps, { logout })(Header)
   ```

9. To clean-up code, add a config helper function to set up and return config function for authentication.
   Update action file for this.
   actions/auth.js

   ```react
   import axios from 'axios'
   
   import {
   	USER_LOADED,
   	USER_LOADING,
   	AUTH_ERROR,
   	LOGIN_SUCCESS,
   	LOGIN_FAIL,
   	LOGOUT_SUCCESS
   } from './types'
   
   // CHECK TOKEN AND LOAD USER
   export const loadUser = () => (dispatch, getState) => {
   	// User Loading
   	dispatch({ type: USER_LOADING })
   
   	axios
   		.get('/api/auth/user', tokenConfig(getState))
   		.then((res) => {
   			dispatch({
   				type: USER_LOADED,
   				payload: res.data
   			})
   		})
   		.catch((err) => {
   			// add error handling dispatch here
   
   			dispatch({ type: AUTH_ERROR })
   		})
   }
   
   // LOGIN USER
   export const login = (username, password) => (dispatch) => {
   	const config = {
   		headers: {
   			'Content-type': 'application/json'
   		}
   	}
   
   	// Request Body
   	const body = JSON.stringify({ username, password })
   
   	axios
   		.post('/api/auth/login', body, config)
   		.then((res) => {
   			dispatch({
   				type: LOGIN_SUCCESS,
   				payload: res.data
   			})
   		})
   		.catch((err) => {
   			// add error handling dispatch here
   
   			dispatch({ type: LOGIN_FAIL })
   		})
   }
   
   // LOGOUT USER
   export const logout = () => (dispatch, getState) => {
   	axios
   		.post('/api/auth/logout', null, tokenConfig(getState))
   		.then((res) => {
   			dispatch({
   				type: LOGOUT_SUCCESS
   			})
   		})
   		.catch((err) => {
   			// add error handling dispatch here
   			console.log(err)
   		})
   }
   
   // Setup config with token - helper function
   export const tokenConfig = (getState) => {
   	// Get token from state
   	const token = getState().auth.token
   
   	const config = {
   		headers: {
   			'Content-Type': 'application/json'
   		}
   	}
   
   	//  If token, add to headers config
   	if (token) {
   		config.headers['Authorization'] = `Token ${token}`
   	}
   
   	return config
   }
   ```

10. Add action types for registering user.
    actions/types.js

    ```react
    export const REGISTER_SUCCESS = 'REGISTER_SUCCESS'
    export const REGISTER_FAIL = 'REGISTER_FAIL'
    ```

11. Create action to register user.
    actions/auth.js

    ```react
    // REGISTER USER
    export const register = ({ username, email, password }) => (dispatch) => {
    	// Headers
    	const config = {
    		headers: {
    			'Content-type': 'application/json'
    		}
    	}
    
    	// Request Body
    	const body = JSON.stringify({ username, email, password })
    
    	axios
    		.post('/api/auth/register', body, config)
    		.then((res) => {
    			dispatch({
    				type: REGISTER_SUCCESS,
    				payload: res.data
    			})
    		})
    		.catch((err) => {
    			// add error handling dispatch here
    
    			dispatch({ type: REGISTER_FAIL })
    		})
    }
    ```

12. Handle Register actions in the reducer for register action types.
    reducers/auth.js

    ```react
    import {
    	USER_LOADED,
    	USER_LOADING,
    	AUTH_ERROR,
    	LOGIN_FAIL,
    	LOGIN_SUCCESS,
    	LOGOUT_SUCCESS,
    	REGISTER_FAIL,
    	REGISTER_SUCCESS
    } from '../actions/types'
    
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
    		case LOGIN_SUCCESS:
    		case REGISTER_SUCCESS:
    			localStorage.setItem('token', action.payload.token)
    			return {
    				...state,
    				...action.payload,
    				isAuthenticated: true,
    				isLoading: false
    			}
    		case AUTH_ERROR:
    		case LOGIN_FAIL:
    		case LOGOUT_SUCCESS:
    		case REGISTER_FAIL:
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

13. Call the register action in the component.
    Register.js

    ```react
    import React, { Fragment, useState } from 'react'
    import { Link, Redirect } from 'react-router-dom'
    import { register } from '../../../actions/auth'
    import { connect } from 'react-redux'
    
    const Register = ({ isAuthenticated, register }) => {
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
    		const { username, email, password, password2 } = userInfo
    		if (password !== password2) {
    			// add error handling toast here
    			console.log("passwords don't match")
    		} else {
    			const newUser = {
    				username,
    				email,
    				password
    			}
    			register(newUser)
    		}
    	}
    
        // Redirect to dashboard after/if registered
    	if (isAuthenticated) {
    		return <Redirect to="/" />
    	}
    
    	return (
    		<Fragment>
    			<div className="row">
    				<div className="col-lg-10 col-xl-9 mx-auto">
    					<div className="card card-signin flex-row my-5">
    						<div className="card-img-left d-none d-md-flex" />
    						<div className="card-body">
    							<h5 className="card-title text-center">Register</h5>
    							<form className="form-signin" onSubmit={onSubmit}>
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
    
    const mapStateToProps = (state) => ({
    	isAuthenticated: state.auth.isAuthenticated
    })
    
    export default connect(mapStateToProps, { register })(Register)
    ```

14. Update other actions to add authentication config token.
    Import tokenConfig function and add config object to all the api calls.

    ```react
    import axios from 'axios'
    import { tokenConfig } from './auth'
    
    import {
    	GET_WATCHLISTS,
    	DELETE_WATCHLIST,
    	ADD_WATCHLIST,
    	GET_STOCKS,
    	SHOW_POPUP,
    	DELETE_STOCK,
    	ADD_STOCK,
    	GET_WATCHLIST_FOR_EDIT,
    	SHOW_EDIT_WATCHLIST_POPUP,
    	GET_COMPANIES_DETAILS
    } from './types.js'
    
    export const getWatchlists = () => (dispatch, getState) => {
    	axios
    		.get('./api/watchlists/', tokenConfig(getState))
    		.then((res) => {
    			dispatch({
    				type: GET_WATCHLISTS,
    				payload: res.data
    			})
    		})
    		.catch((err) => console.log(err))
    }
    
    export const deleteWatchlist = (id) => (dispatch, getState) => {
    	axios
    		.delete(`./api/watchlists/${id}/`, tokenConfig(getState))
    		.then((res) => {
    			dispatch({
    				type: DELETE_WATCHLIST,
    				payload: id
    			})
    		})
    		.catch((err) => console.log(err))
    }
    
    export const addWatchlist = (watchlist) => (dispatch, getState) => {
    	axios
    		.post('./api/watchlists/', watchlist, tokenConfig(getState))
    		.then((res) => {
    			dispatch({
    				type: ADD_WATCHLIST,
    				payload: res.data
    			})
    		})
    		.catch((err) => console.log(err))
    }
    
    export const show_Popup = (getWatchlistID, showPopup) => (dispatch) => {
    	dispatch({
    		type: SHOW_POPUP,
    		payload: { showPopup: showPopup, getWatchlistID: getWatchlistID }
    	})
    }
    
    export const getStocks = (id) => (dispatch, getState) => {
    	axios
    		.get(`./api/watchlists-stocks/?watchlist_id=${id}`, tokenConfig(getState))
    		.then((res) => {
    			dispatch({
    				type: GET_STOCKS,
    				payload: res.data
    			})
    		})
    		.catch((err) => console.log(err))
    }
    
    export const deleteWatchlistStock = (id) => (dispatch, getState) => {
    	axios
    		.delete(`./api/watchlists-stocks/${id}/`, tokenConfig(getState))
    		.then((res) => {
    			dispatch({
    				type: DELETE_STOCK,
    				payload: id
    			})
    		})
    		.catch((err) => console.log(err))
    }
    
    export const addWatchlistStock = (stock) => (dispatch, getState) => {
    	axios
    		.post(`./api/watchlists-stocks/`, stock, tokenConfig(getState))
    		.then((res) => {
    			dispatch({
    				type: ADD_STOCK,
    				payload: res.data
    			})
    		})
    		.catch((err) => console.log(err))
    }
    
    export const getCompaniesDetails = () => (dispatch, getState) => {
    	axios
    		.get(`./api/companies/`, tokenConfig(getState))
    		.then((res) => {
    			dispatch({
    				type: GET_COMPANIES_DETAILS,
    				payload: res.data
    			})
    		})
    		.catch((err) => console.log(err))
    }
    
    export const getWatchlistForEdit = (id) => (dispatch, getState) => {
    	axios
    		.get(`./api/watchlists/${id}/`, tokenConfig(getState))
    		.then((res) => {
    			dispatch({
    				type: GET_WATCHLIST_FOR_EDIT,
    				payload: res.data
    			})
    		})
    		.catch((err) => console.log(err))
    }
    
    export const showEditWatchlistPopup = (getWatchlistID, showEditWatchlistPopup) => (dispatch) => {
    	dispatch({
    		type: SHOW_EDIT_WATCHLIST_POPUP,
    		payload: { showEditWatchlistPopup: showEditWatchlistPopup, getWatchlistID: getWatchlistID }
    	})
    }
    ```

    

