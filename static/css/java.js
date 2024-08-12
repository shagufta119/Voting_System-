const data = {
    voter_id: "some_voter_id",
    candidate: "selected_candidate"
};
fetch('/submit_vote', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})
