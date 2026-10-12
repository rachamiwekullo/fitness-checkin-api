const form = document.querySelector("#checkin-form");
const message = document.querySelector("#message");
const list = document.querySelector("#checkin-list");

async function refreshCheckins() {
  const response = await fetch("/api/checkins");
  if (!response.ok) throw new Error(`Could not load check-ins (${response.status}).`);
  const checkins = await response.json();
  list.replaceChildren();
  for (const checkin of checkins) {
    const item = document.createElement("li");
    item.textContent = `${checkin.name}: ${checkin.steps.toLocaleString()} steps — ${
      checkin.hit_goal ? "goal reached" : "below target"
    }`;
    list.append(item);
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!form.reportValidity()) return;

  const values = new FormData(form);
  const payload = {
    name: values.get("name"),
    sleep: Number(values.get("sleep")),
    water: Number(values.get("water")),
    steps: Number(values.get("steps")),
  };
  try {
    const response = await fetch("/api/checkins", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    if (!response.ok) {
      const detail = await response.json();
      throw new Error(detail.detail?.[0]?.msg ?? `Request failed (${response.status}).`);
    }
    await refreshCheckins();
    message.textContent = "Check-in saved.";
    form.reset();
  } catch (error) {
    message.textContent = error instanceof Error ? error.message : "Unexpected request failure.";
  }
});

refreshCheckins().catch((error) => {
  message.textContent = error instanceof Error ? error.message : "Could not load check-ins.";
});
