import React from 'react'

import meetup_icon from "../../images/meetup.png";
import facebook_icon from "../../images/facebook.png";
import tmi_labs_icon from "../../images/tmi_labs_logo.png";

class NotFoundPage extends React.Component {

  constructor(props) {
    super(props)
    this.handle_home = this.handle_home.bind(this)
  }

  handle_home(e) {
    console.log("SIGNUP")
    top.location="http://hackademy.ai"
    return null
  }

  render() {
    return (      
      <div className="site">
        <div className="wrapper">
          <h1>Hackademy.ai</h1>          
          <h2>Error #404: The page you were looking for does not exist.</h2>
          <div>
            <button className="red button" onClick={this.handle_home}><span>Home</span></button>            
          </div>
        </div>
        <div className="footer">
          <div className="border"></div>
          <div className="pull-left">
            <h1>
              <a href="https://bit.ly/hackademy_ai_tmi">
                "Let's talk about that brilliant idea of yours!"
              </a>
            </h1>
          </div>
          <div className="pull-right">
            <a href="https://bit.ly/hackademy_ai_tmi">
              <img src={tmi_labs_icon} alt="the main ingredient labs"/>
            </a>
          </div>
        </div>
      </div>
    )
  }
}

export default NotFoundPage
