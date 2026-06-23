// ============================================
// VERSION 1: Using .then().catch()
// ============================================

function fetchTodoWithThen() {
  fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then((response) => {
      // Check if HTTP status is OK (200-299)
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json(); // parse JSON body
    })
    .then((data) => {
      console.log('--- .then().catch() version ---');
      console.log('id:', data.id);
      console.log('title:', data.title);
      console.log('completed:', data.completed);
    })
    .catch((error) => {
      // Runs if fetch fails (network error) OR if we threw above (bad status)
      // OR if response.json() fails to parse
      console.error('Error fetching todo (then/catch):', error.message);
    });
}


// ============================================
// VERSION 2: Using async/await with try/catch
// ============================================

async function fetchTodoWithAsync() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    console.log('--- async/await version ---');
    console.log('id:', data.id);
    console.log('title:', data.title);
    console.log('completed:', data.completed);
  } catch (error) {
    // Catches network failures, thrown errors, and JSON parse errors
    console.error('Error fetching todo (async/await):', error.message);
  }
}


// ============================================
// Run both
// ============================================

fetchTodoWithThen();
fetchTodoWithAsync();


// ============================================
// NOTES on error handling
// ============================================
// 1. fetch() only rejects on NETWORK failures (e.g. no internet, DNS error,
//    server unreachable). It does NOT reject on HTTP error statuses like
//    404 or 500 — those still resolve successfully, just with response.ok
//    set to false. That's why we manually check `response.ok` and throw.
// 2. response.json() can also fail/reject if the body isn't valid JSON.
// 3. In the .then() chain, any thrown error or rejected promise anywhere
//    upstream gets caught by the single .catch() at the end.
// 4. In async/await, any of those same failures are caught by the single
//    try/catch block.
