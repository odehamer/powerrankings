# Fantasy Football Power Rankings

A client-side web application for creating power rankings for your Sleeper fantasy football league using head-to-head team comparisons with an efficient merge sort algorithm.

## Features

- **Direct Sleeper API Integration**: Fetches live data from your Sleeper fantasy football league
- **Interactive Team Comparisons**: Compare teams head-to-head to create personalized rankings
- **Efficient Merge Sort Algorithm**: Minimizes the number of comparisons needed
- **Real-time League Validation**: Instantly validates league IDs and shows team previews
- **Client-side Only**: No server required - runs entirely in your browser
- **Modern UI**: Clean, responsive interface with team avatars and statistics

## How to Use

1. **Open the App**: Open `base.html` in any modern web browser
2. **Enter League ID**: Input your Sleeper league ID (found in your league URL or settings)
3. **Preview Teams**: The app will fetch and display all teams in your league
4. **Start Rankings**: Click "Start Power Rankings" to begin the comparison process
5. **Make Comparisons**: Choose between pairs of teams when prompted
6. **View Results**: See your final power rankings with crown for the #1 team!

## Files

- `base.html` - Main page for league input and API validation
- `league_detail.html` - Power rankings interface with merge sort algorithm
- `test.py` - Original Python script (reference implementation)

## Technical Details

### Algorithm
- Uses a modified merge sort algorithm for optimal team comparisons
- Stores comparison results to avoid asking the same question twice
- Minimizes total comparisons needed: approximately n*log(n) where n is number of teams

### API Integration
- Fetches data directly from Sleeper's public API
- No authentication required
- Real-time validation of league IDs
- Handles errors gracefully with user feedback

### Browser Compatibility
- Works in all modern browsers (Chrome, Firefox, Safari, Edge)
- Uses ES6+ features (async/await, fetch API)
- Responsive design for mobile and desktop

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/odehamer/powerrankings.git
   cd powerrankings
   ```

2. Open `base.html` in your web browser

3. Enter your Sleeper league ID and start ranking!

## Finding Your League ID

Your Sleeper league ID can be found in:
- The URL when viewing your league in a web browser
- League settings in the Sleeper mobile app
- It's a long number (typically 15+ digits)

Example: `1254922727656001536`

## Development

This is a pure client-side application with no build process required. Simply edit the HTML files and refresh your browser.

### Project Structure
```
powerrankings/
├── base.html           # Main entry point
├── league_detail.html  # Ranking interface
├── test.py            # Original Python implementation
└── README.md          # This file
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - see the code for details.
