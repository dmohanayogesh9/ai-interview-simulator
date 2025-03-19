<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Role Selection</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="d-flex justify-content-center align-items-center vh-100">
    <div class="card p-4 shadow-lg" style="width: 400px;">
        <h2 class="text-center mb-4">Select Your Role</h2>
        <form id="roleForm">  <!-- Fixed: Added ID and removed action="/" -->
            <div class="mb-3">
                <label for="role" class="form-label">Choose Role:</label>
                <select class="form-select" id="role" name="role" required>
                    <option value="" disabled selected>Select a role</option>
                    <option value="Front-End Developer">Front-End Developer</option>
                    <option value="Back-End Developer">Back-End Developer</option>
                    <option value="Full-Stack Developer">Full-Stack Developer</option>
                    <option value="Mobile Developer">Mobile Developer</option>
                    <option value="Data Scientist">Data Scientist</option>
                    <option value="Data Analyst">Data Analyst</option>
                    <option value="Machine Learning Engineer">Machine Learning Engineer</option>
                    <option value="DevOps Engineer">DevOps Engineer</option>
                    <option value="Cloud Engineer">Cloud Engineer</option>
                    <option value="Cybersecurity Analyst">Cybersecurity Analyst</option>
                    <option value="UX/UI Designer">UX/UI Designer</option>
                    <option value="Quality Assurance (QA) Engineer">Quality Assurance (QA) Engineer</option>
                    <option value="Blockchain Developer">Blockchain Developer</option>
                    <option value="AI Research Scientist">AI Research Scientist</option>
                    <option value="AI Engineer">AI Engineer</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary w-100">Start Interview</button>
        </form>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const form = document.getElementById("roleForm");

            form.addEventListener("submit", async (event) => {
                event.preventDefault();  // Prevent default form submission

                const selectedRole = document.getElementById("role").value;

                if (!selectedRole) {
                    alert("Please select a role.");
                    return;
                }

                try {
                    const response = await fetch("http://127.0.0.1:5000/role", {  // Fixed: Removed extra space
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({ role: selectedRole }),
                    });

                    if (response.msg) {
                        window.location.href = "index.html";  
                    } else {
                        alert("An error occurred. Please try again.");
                    }
                } catch (error) {
                    alert("An error occurred. Please try again.");
                }
            });
        });
    </script>
</body>
</html>
