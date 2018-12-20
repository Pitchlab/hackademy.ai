import React from 'react'
import Link from 'gatsby-link'

import meetup_icon from "../../images/meetup.png";
import facebook_icon from "../../images/facebook.png";
import tmi_labs_icon from "../../images/tmi_labs_logo.png";
import tmi_logo from "../../images/tmi_logo.png";

class IndexPage extends React.Component {

  constructor(props) {
    super(props)
    this.handle_signup = this.handle_signup.bind(this)
    this.handle_download = this.handle_download.bind(this)
  }

  handle_signup(e) {
    console.log("SIGNUP")
    top.location="http://bit.ly/hackademy_apply"
    return null
  }

  handle_download(e) {
    console.log("DOWNLOAD")
    top.location.href="http://bit.ly/hackademy_ai_guide"
    return null
  }

  render() {
    return <div className="site">
        <div className="wrapper">
          <h1>Hackademy.ai</h1>
          <h2>
            edition #2: <span className="topic">Predictive modelling</span> with <span className="topic">
              ING
            </span>
          </h2>
          <div>
            <button className="red button" onClick={this.handle_signup}>
              <span>Apply now!</span>
            </button>
            <button className="button" onClick={this.handle_download}>
              <span>Download Guide</span>
            </button>
          </div>
          <div className="code">
            <ul>
              <li>
                <div className="file">event.py</div>
                event = &#123;
                <ul>
                  <li>
                    <span className="string">"name"</span> : <span className="string">
                      "hackademy.ai"
                    </span>,
                  </li>
                  <li>
                    <span className="string">"about"</span>: <span className="string">
                      "a practical ai hackathon "
                    </span>\<br />
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span className="string">
                      "for developers that want "
                    </span>\<br />
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span className="string">
                      "to get hands-on with ai "
                    </span>
                  </li>
                  <li>
                    <span className="string">"date"</span>: <span className="string">
                      "Friday Jan 31, 2019"
                    </span>,
                  </li>
                  <li>
                    <span className="string">"start_time"</span>: <span className="string">
                      "2019-01-31T13:00:00+02:00"
                    </span>,
                  </li>
                  <li>
                    <span className="string">"end_time"</span>: <span className="string">
                      "2019-01-31T19:00:00+02:00"
                    </span>,
                  </li>
                  <li>
                    <span className="string">"venue"</span>: <span className="string">
                      "The Main Ingredient"
                    </span>,
                  </li>
                  <li>
                    <span className="string">"location"</span>: <span className="string">
                      "Amsterdam"
                    </span>,
                  </li>
                  <li>
                    <span className="string">"topic"</span>: <span className="string">
                      "predictive modelling"
                    </span>,
                  </li>
                  <li>
                    <span className="string">"price"</span>: <span className="string">
                      "&eur;15,-"
                    </span>,
                  </li>
                  <li>
                    <span className="string">"max_participants"</span>: <span className="number">
                      15
                    </span>,
                  </li>
                  <li>
                    <span className="string">"contact"</span>: <span className="string">
                      "https://www.meetup.com/Hackademy-ai/"
                    </span>
                  </li>
                </ul>
                &#125;
              </li>
            </ul>
          </div>
          <div className="links">
            <ul>
              <li>
                <a href="https://www.facebook.com/ai.hackademy/">
                  <img src={facebook_icon} alt="facebook" />
                </a>
              </li>
              <li>
                <a href="https://meetup.com/Hackademy-ai">
                  <img src={meetup_icon} alt="meetup" />
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div className="footer">
          <div className="border" />
          <div className="pull-left">
            <h1>
              <a href="https://bit.ly/hackademy_ai_tmi">
                "Let's talk about that brilliant idea of yours!"
              </a>
            </h1>
          </div>
          <div className="pull-right">
            <a href="https://bit.ly/hackademy_ai_tmi">
              <img src={tmi_logo} alt="the main ingredient labs" />
            </a>
          </div>
        </div>
      </div>
  }
}

export default IndexPage
