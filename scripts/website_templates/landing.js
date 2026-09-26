/* claude-howto landing — progress tracking, terminal, scroll effects.
   Vanilla JS, no dependencies. The page is fully usable without it:
   every lesson link navigates, and interactive controls are hidden via
   the `no-js` class on <html>. */
(function () {
  "use strict";

  var root = document.documentElement;
  root.classList.remove("no-js");
  root.classList.add("js");

  var STORAGE_KEY = "claude-howto.progress.v1";
  var VALID_STATUS = { "not-started": true, "in-progress": true, "done": true };
  var STATUS_LABEL = {
    "not-started": "Not started",
    "in-progress": "In progress",
    done: "Done",
  };

  var reducedMotion = false;
  try {
    reducedMotion = window.matchMedia(
      "(prefers-reduced-motion: reduce)"
    ).matches;
  } catch (e) {
    /* matchMedia unavailable — treat as no preference */
  }

  /* ================= Theme (shared with the docs pages) =================
     Same localStorage key and `dark` class on <html> as page.html.j2.
     The pre-paint inline script already applied the initial theme; this
     wires the toggle and follows the OS scheme while nothing is saved. */

  var THEME_KEY = "claude-howto-theme";
  var themeToggle = document.getElementById("theme-toggle");

  function currentTheme() {
    return root.classList.contains("dark") ? "dark" : "light";
  }

  function paintThemeToggle() {
    if (!themeToggle) return;
    themeToggle.setAttribute(
      "aria-label",
      currentTheme() === "dark"
        ? "Switch to light theme"
        : "Switch to dark theme"
    );
  }

  function savedTheme() {
    try {
      return window.localStorage.getItem(THEME_KEY);
    } catch (e) {
      return null;
    }
  }

  function applyTheme(theme, animate) {
    if (animate && !reducedMotion) {
      root.classList.add("theme-anim");
      window.setTimeout(function () {
        root.classList.remove("theme-anim");
      }, 350);
    }
    root.classList.toggle("dark", theme === "dark");
    paintThemeToggle();
  }

  if (themeToggle) {
    themeToggle.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      applyTheme(next, true);
      try {
        window.localStorage.setItem(THEME_KEY, next);
      } catch (e) {}
    });
  }
  paintThemeToggle();

  /* No saved choice: follow prefers-color-scheme changes live. */
  try {
    var themeMq = window.matchMedia("(prefers-color-scheme: dark)");
    var followOsTheme = function (e) {
      if (!savedTheme()) applyTheme(e.matches ? "dark" : "light", true);
    };
    if (themeMq.addEventListener) {
      themeMq.addEventListener("change", followOsTheme);
    } else if (themeMq.addListener) {
      themeMq.addListener(followOsTheme);
    }
  } catch (e) {}

  /* ================= Progress store ================= */

  var mem = { v: 1, lessons: {} };
  var persist = true;

  function loadState() {
    if (!persist) return;
    try {
      var raw = window.localStorage.getItem(STORAGE_KEY);
      if (!raw) return;
      var data = JSON.parse(raw);
      if (data && data.v === 1 && data.lessons && typeof data.lessons === "object") {
        mem.lessons = data.lessons;
      }
    } catch (e) {
      persist = false;
    }
  }

  function saveState() {
    if (!persist) return;
    try {
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(mem));
    } catch (e) {
      persist = false;
    }
  }

  var lessonEls = Array.prototype.slice.call(
    document.querySelectorAll(".lesson[data-lesson]")
  );
  var stationEls = Array.prototype.slice.call(
    document.querySelectorAll(".station[data-module]")
  );
  var knownIds = {};
  lessonEls.forEach(function (el) {
    knownIds[el.getAttribute("data-lesson")] = true;
  });

  function lessonStatus(id) {
    var rec = mem.lessons[id];
    return rec && VALID_STATUS[rec.s] ? rec.s : "not-started";
  }

  function setStatus(id, status) {
    if (!knownIds[id]) return;
    mem.lessons[id] = { s: status, t: Date.now() };
    saveState();
  }

  function pruneUnknown() {
    var changed = false;
    Object.keys(mem.lessons).forEach(function (id) {
      if (!knownIds[id]) {
        delete mem.lessons[id];
        changed = true;
      }
    });
    if (changed) saveState();
  }

  /* Mark a lesson in progress when the user navigates to it. Shared by
     lesson links, module title links and the Continue/Start button. */
  function markStarted(lessonEl) {
    if (!lessonEl) return;
    var id = lessonEl.getAttribute("data-lesson");
    if (lessonStatus(id) === "not-started") {
      setStatus(id, "in-progress");
      paintAll();
    }
  }

  /* Mark on left-click (incl. ctrl/cmd-click — navigation still proceeds)
     and on middle-click, which fires `auxclick` with button 1. */
  function bindMarkStarted(el, getLessonEl) {
    el.addEventListener("click", function () {
      markStarted(getLessonEl());
    });
    el.addEventListener("auxclick", function (e) {
      if (e.button === 1) markStarted(getLessonEl());
    });
  }

  /* ================= Painting ================= */

  function paintLesson(el) {
    var id = el.getAttribute("data-lesson");
    var status = lessonStatus(id);
    el.setAttribute("data-status", status);
    var check = el.querySelector(".check");
    if (check) {
      check.setAttribute(
        "aria-checked",
        status === "done" ? "true" : status === "in-progress" ? "mixed" : "false"
      );
    }
    var label = el.querySelector("[data-lstatus]");
    if (label) label.textContent = STATUS_LABEL[status];
  }

  function paintStation(station) {
    var rows = station.querySelectorAll(".lesson[data-lesson]");
    var total = rows.length;
    var done = 0;
    var started = 0;
    for (var i = 0; i < total; i++) {
      var s = lessonStatus(rows[i].getAttribute("data-lesson"));
      if (s === "done") {
        done++;
        started++;
      } else if (s === "in-progress") {
        started++;
      }
    }
    var status =
      total > 0 && done === total
        ? "done"
        : started > 0
          ? "in-progress"
          : "not-started";
    station.setAttribute("data-status", status);
    var pill = station.querySelector("[data-pill]");
    if (pill) pill.textContent = STATUS_LABEL[status];
    var count = station.querySelector("[data-count]");
    if (count) count.textContent = done + "/" + total;
    var bar = station.querySelector("[data-bar]");
    if (bar) bar.style.width = total ? (done / total) * 100 + "%" : "0%";
  }

  var RING_R = 52;
  var RING_C = 2 * Math.PI * RING_R;
  var continueTarget = null;

  function paintOverall() {
    var total = lessonEls.length;
    var done = 0;
    var inProgress = 0;
    var continueEl = null;
    var continueTime = -1;
    var firstTodo = null;

    lessonEls.forEach(function (el) {
      var id = el.getAttribute("data-lesson");
      var s = lessonStatus(id);
      if (s === "done") {
        done++;
      } else if (s === "in-progress") {
        inProgress++;
        var t = mem.lessons[id] && mem.lessons[id].t ? mem.lessons[id].t : 0;
        if (t > continueTime) {
          continueTime = t;
          continueEl = el;
        }
      } else if (!firstTodo) {
        firstTodo = el;
      }
    });

    var pct = total ? Math.round((done / total) * 100) : 0;
    var ring = document.getElementById("ring-fg");
    if (ring) {
      ring.style.strokeDashoffset = String(RING_C * (1 - done / (total || 1)));
    }
    var pctEl = document.getElementById("ring-pct");
    if (pctEl) pctEl.textContent = pct + "%";
    var doneEl = document.getElementById("c-done");
    if (doneEl) doneEl.textContent = String(done);
    var progEl = document.getElementById("c-prog");
    if (progEl) progEl.textContent = String(inProgress);
    var todoEl = document.getElementById("c-todo");
    if (todoEl) todoEl.textContent = String(total - done - inProgress);

    var continueBtn = document.getElementById("continue-btn");
    var allDone = document.getElementById("all-done");
    var target = continueEl || firstTodo;
    continueTarget = target;
    if (continueBtn && allDone) {
      if (target && done < total) {
        var link = target.querySelector(".lesson-link");
        var title = link ? link.textContent.trim() : "";
        var station = target.closest(".station");
        var modTitle = "";
        if (station) {
          var t = station.querySelector(".station-title");
          modTitle = t ? t.textContent.trim() : "";
        }
        var verb = done + inProgress === 0 ? "Start" : "Continue";
        continueBtn.hidden = false;
        allDone.hidden = true;
        if (link) continueBtn.setAttribute("href", link.getAttribute("href"));
        continueBtn.textContent =
          verb + ": " + (modTitle ? modTitle + " · " : "") + title;
      } else {
        continueBtn.hidden = true;
        allDone.hidden = false;
      }
    }
    paintTrack();
  }

  function paintTrack() {
    var fill = document.getElementById("track-fill");
    var subway = document.getElementById("subway");
    if (!fill || !subway) return;

    var rect = subway.getBoundingClientRect();
    if (rect.height <= 0) return;

    // Furthest started station keeps the line lit even above the scroll mark.
    var statusP = 0;
    stationEls.forEach(function (st) {
      if (st.getAttribute("data-status") === "not-started") return;
      var node = st.querySelector(".node") || st;
      var y = node.getBoundingClientRect().top - rect.top;
      if (y > 0) statusP = Math.max(statusP, Math.min(1, y / rect.height));
    });

    var scrollP = Math.min(
      1,
      Math.max(0, (window.innerHeight * 0.8 - rect.top) / rect.height)
    );

    fill.style.height = Math.max(scrollP, statusP) * 100 + "%";
  }

  function paintAll() {
    lessonEls.forEach(paintLesson);
    stationEls.forEach(paintStation);
    paintOverall();
  }

  /* ================= Events ================= */

  lessonEls.forEach(function (el) {
    var id = el.getAttribute("data-lesson");

    var check = el.querySelector(".check");
    if (check) {
      check.addEventListener("click", function () {
        var s = lessonStatus(id);
        setStatus(id, s === "done" ? "in-progress" : "done");
        paintAll();
      });
    }

    var link = el.querySelector(".lesson-link");
    if (link) {
      bindMarkStarted(link, function () {
        return el;
      });
    }
  });

  function setExpanded(station, expanded) {
    var toggle = station.querySelector(".station-toggle");
    var list = station.querySelector(".lessons");
    if (!toggle || !list) return;
    toggle.setAttribute("aria-expanded", String(expanded));
    list.hidden = !expanded;
  }

  stationEls.forEach(function (station) {
    var toggle = station.querySelector(".station-toggle");
    if (!toggle) return;

    // Collapse by default; in-progress modules are re-expanded after the
    // first paint once their status is known (see init below).
    setExpanded(station, false);

    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      setExpanded(station, !open);
    });

    // The module title links to the module page; treat it like opening its
    // first lesson (Overview).
    var titleLink = station.querySelector(".station-title a");
    if (titleLink) {
      bindMarkStarted(titleLink, function () {
        return station.querySelector(".lesson[data-lesson]");
      });
    }
  });

  var continueBtnEl = document.getElementById("continue-btn");
  if (continueBtnEl) {
    bindMarkStarted(continueBtnEl, function () {
      return continueTarget;
    });
  }

  var resetBtn = document.getElementById("reset-btn");
  if (resetBtn) {
    resetBtn.addEventListener("click", function () {
      if (!window.confirm("Reset all lesson progress? This cannot be undone.")) {
        return;
      }
      mem.lessons = {};
      saveState();
      paintAll();
    });
  }

  /* Cross-tab sync + bfcache restore. */
  window.addEventListener("storage", function (e) {
    if (e.key === THEME_KEY && e.newValue) {
      applyTheme(e.newValue, true);
      return;
    }
    if (e.key !== STORAGE_KEY) return;
    mem.lessons = {};
    persist = true;
    loadState();
    pruneUnknown();
    paintAll();
  });

  window.addEventListener("pageshow", function () {
    mem.lessons = {};
    loadState();
    pruneUnknown();
    paintAll();
  });

  var scrollTicking = false;
  window.addEventListener(
    "scroll",
    function () {
      if (scrollTicking) return;
      scrollTicking = true;
      window.requestAnimationFrame(function () {
        paintTrack();
        scrollTicking = false;
      });
    },
    { passive: true }
  );
  window.addEventListener("resize", paintTrack);

  /* ================= Terminal typing ================= */

  function runTerminal() {
    var term = document.getElementById("terminal");
    if (!term || reducedMotion) return;

    var lines = Array.prototype.slice.call(term.querySelectorAll(".t-line"));
    var typed = lines.map(function (line) {
      var tt = line.querySelector(".t-tt");
      var text = tt ? tt.textContent : "";
      return { line: line, tt: tt, text: text, isCmd: !!tt };
    });

    function reset() {
      typed.forEach(function (item) {
        item.line.style.visibility = "hidden";
        item.line.classList.remove("t-caret");
        if (item.tt) {
          item.tt.textContent = "";
          item.tt.classList.remove("t-typing");
        }
      });
    }

    var delays = [];
    function later(fn, ms) {
      delays.push(window.setTimeout(fn, ms));
    }

    function play() {
      reset();
      var t = 350;
      typed.forEach(function (item) {
        if (item.isCmd) {
          // Command lines type character by character.
          var text = item.text;
          var start = t;
          for (var i = 0; i <= text.length; i++) {
            (function (it, ch) {
              later(function () {
                it.line.style.visibility = "visible";
                it.tt.textContent = text.slice(0, ch);
                it.tt.classList.add("t-typing");
              }, start + ch * 38);
            })(item, i);
          }
          t += text.length * 38 + 420;
          (function (it) {
            later(function () {
              it.tt.classList.remove("t-typing");
            }, t - 380);
          })(item);
        } else {
          // Output lines appear at once.
          (function (it, at) {
            later(function () {
              it.line.style.visibility = "visible";
            }, at);
          })(item, t);
          t += 260;
        }
      });
      // Leave the caret blinking on the final prompt, hold, then loop.
      var last = typed[typed.length - 1];
      if (last && last.tt) {
        later(function () {
          last.line.classList.add("t-caret");
        }, t);
      }
      later(play, t + 6500);
    }
    play();
  }

  /* ================= Reveal on scroll ================= */

  var revealEls = Array.prototype.slice.call(
    document.querySelectorAll(".reveal")
  );
  if ("IntersectionObserver" in window && !reducedMotion) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -6% 0px" }
    );
    revealEls.forEach(function (el) {
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("in");
    });
  }

  /* ================= Mobile nav ================= */

  var navToggle = document.getElementById("nav-toggle");
  var navMenu = document.getElementById("nav-menu");
  if (navToggle && navMenu) {
    navToggle.addEventListener("click", function () {
      var open = navMenu.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", String(open));
    });
    navMenu.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        navMenu.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && navMenu.classList.contains("open")) {
        navMenu.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.focus();
      }
    });
  }

  /* ================= Copy buttons ================= */

  Array.prototype.slice
    .call(document.querySelectorAll("[data-copy]"))
    .forEach(function (btn) {
      btn.addEventListener("click", function () {
        var text = btn.getAttribute("data-copy") || "";
        function feedback() {
          var label = btn.querySelector(".copy-label");
          btn.classList.add("copied");
          if (label) {
            var prev = label.textContent;
            label.textContent = "Copied";
            window.setTimeout(function () {
              label.textContent = prev;
              btn.classList.remove("copied");
            }, 1400);
          }
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(feedback, feedback);
        } else {
          var ta = document.createElement("textarea");
          ta.value = text;
          ta.style.position = "fixed";
          ta.style.opacity = "0";
          document.body.appendChild(ta);
          ta.select();
          try {
            document.execCommand("copy");
          } catch (e) {
            /* clipboard unavailable — still show feedback */
          }
          document.body.removeChild(ta);
          feedback();
        }
      });
    });

  /* ================= Init ================= */

  loadState();
  pruneUnknown();
  paintAll();
  stationEls.forEach(function (station) {
    if (station.getAttribute("data-status") === "in-progress") {
      setExpanded(station, true);
    }
  });
  paintTrack();
  runTerminal();
})();
