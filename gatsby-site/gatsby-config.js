module.exports = {
  pathPrefix: '/hackademy.ai',
  siteMetadata: {
    title: 'Hackademy.ai',
  },
  plugins: [
    {
      resolve: 'gatsby-plugin-react-helmet',
    },
    {
      resolve: 'gatsby-plugin-sass',
    },
    {
      resolve: 'gatsby-plugin-google-analytics',
      options: {
        trackingId: "YOUR_GOOGLE_ANALYTICS_TRACKING_ID",
        // Puts tracking script in the head instead of the body
        head: false,
        // Setting this parameter is optional
        anonymize: true,
        // Setting this parameter is also optional
        respectDNT: true,
        // Avoids sending pageview hits from custom paths
        exclude: ["/preview/**", "/do-not-track/me/too/"],
      },
    },
    {
      resolve: `gatsby-plugin-google-fonts`,
      options: {
        fonts: [
          'Roboto',
          'Roboto\:300,400,400i,700', // you can also specify font weights and styles
          'Roboto Mono',
          'Roboto+Mono\:300,400,400i,700' // you can also specify font weights and styles
        ]
      }
    }
  ],
}
