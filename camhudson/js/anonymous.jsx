import React from 'react';
import PropTypes from 'prop-types';

// EXAMPLE: This is a note on what this syntax means
// // This line automatically assigns this.props.url to the const variable url
// const { url } = this.props; // NOTE: Braces look for var of same name within object on right


class AnonymousMessage extends React.Component {
    constructor(props) {
        // FIXME: Not sure if I need any props stuff since I don't need props
        super(props);
        // this.toggleAnonymous = this.toggleAnonymous.bind(this);
    }

    // NOTE: This doesn't need to be JS because there's no API call necessary. Just use HTML.
    // toggleAnonymous() {
    //     const { toggleAnonymous } = this.props;
        
    // }

    render() {
        return (
            <div class="container">
                <form>
                    <div class="form-group">
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="check1" value="anonymous" checked />
                            <label class="form-check-label" for="check1">Send anonymously</label>
                        </div>
                        <div id="email-box">    
                            <label for="email-address">Email address</label>
                            <input type={this.state.email ? "email" : "hidden"} class="form-control" id="email-address" aria-describedby="email-help" placeholder="Optional (check &quot;Send anonymously&quot; if you don't want to share this information)" />
                            <small id="email-help" class="form-text text-muted">We'll never share your email with anyone else.</small>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="message">Password</label>
                        <input type="password" class="form-control" id="message" placeholder="What's on your mind?" />
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        );
    }
}