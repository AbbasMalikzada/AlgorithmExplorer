// ─────────────────────────────────────────────────────
// PhoneBook Algorithm Explorer — Interactive Script
// ─────────────────────────────────────────────────────

// hey

const COLORS = [
  '#FF6B6B','#FF9F43','#FECA57','#48DBFB','#FF9FF3',
  '#54A0FF','#5F27CD','#00D2D3','#1DD1A1','#C8D6E5'
];

// ═══════════════════════════════════════════════════════
//  TAB NAVIGATION
// ═══════════════════════════════════════════════════════
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
    const target = document.getElementById('tab-' + btn.dataset.tab);
    if (target) {
      target.classList.add('active');
      target.querySelectorAll('.glass-card').forEach((card, i) => {
        card.style.animation = 'none';
        card.offsetHeight; // reflow
        card.style.animation = `fadeInUp 0.4s ease-out ${i * 0.06}s both`;
      });
    }
  });
});

// ═══════════════════════════════════════════════════════
//  CODE TAB — Sub-section pills
// ═══════════════════════════════════════════════════════
document.querySelectorAll('.algo-pill[data-code]').forEach(pill => {
  pill.addEventListener('click', () => {
    document.querySelectorAll('.algo-pill[data-code]').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.code-section').forEach(s => s.style.display = 'none');
    pill.classList.add('active');
    const sec = document.getElementById('code-' + pill.dataset.code);
    if (sec) sec.style.display = 'block';
  });
});

// ═══════════════════════════════════════════════════════
//  SEARCH TAB — Algorithm pills
// ═══════════════════════════════════════════════════════
let currentSearchAlgo = 'linear';
document.querySelectorAll('.algo-pill[data-search]').forEach(pill => {
  pill.addEventListener('click', () => {
    document.querySelectorAll('.algo-pill[data-search]').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    currentSearchAlgo = pill.dataset.search;
    const titleEl = document.getElementById('search-algo-title');
    if (currentSearchAlgo === 'linear') {
      titleEl.textContent = '🔎 Linear Search — O(n)';
      document.getElementById('explain-linear').style.display = '';
      document.getElementById('explain-binary').style.display = 'none';
    } else {
      titleEl.textContent = '⚡ Binary Search — O(log n)';
      document.getElementById('explain-linear').style.display = 'none';
      document.getElementById('explain-binary').style.display = '';
    }
    resetSearch();
  });
});

// ═══════════════════════════════════════════════════════
//  SEARCH DEMO
// ═══════════════════════════════════════════════════════
const SEARCH_DATA = [
  'Alice','Bob','Charlie','Diana','Eve','Frank','Grace','Hank','Ivy','Jack'
];

let searchSpeed = 400;
let searchTimer = null;

// Speed buttons
document.querySelectorAll('[data-search-speed]').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('[data-search-speed]').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    searchSpeed = parseInt(btn.dataset.searchSpeed);
  });
});

function renderSearchItems(data) {
  const container = document.getElementById('searchItems');
  container.innerHTML = '';
  data.forEach((name, i) => {
    const el = document.createElement('div');
    el.className = 'search-item';
    el.id = 'si-' + i;
    el.innerHTML = `<span class="item-index">[${i}]</span>${name}`;
    container.appendChild(el);
  });
}

function resetSearch() {
  clearTimeout(searchTimer);
  const data = currentSearchAlgo === 'binary' ? [...SEARCH_DATA].sort() : [...SEARCH_DATA];
  renderSearchItems(data);
  document.getElementById('searchStatus').textContent = 'Enter a name and click Search';
  document.getElementById('searchStatus').style.background = 'rgba(255,255,255,0.08)';
  document.getElementById('searchStatus').style.color = '';
  document.getElementById('searchPlayBtn').disabled = false;
}

function startSearch() {
  const target = document.getElementById('searchInput').value.trim();
  if (!target) { alert('Please enter a name to search for.'); return; }

  document.getElementById('searchPlayBtn').disabled = true;
  const data = currentSearchAlgo === 'binary' ? [...SEARCH_DATA].sort() : [...SEARCH_DATA];
  renderSearchItems(data);

  if (currentSearchAlgo === 'linear') {
    runLinearSearch(data, target);
  } else {
    runBinarySearch(data, target);
  }
}

function runLinearSearch(data, target) {
  let i = 0;
  const status = document.getElementById('searchStatus');

  function step() {
    if (i > 0) {
      const prev = document.getElementById('si-' + (i - 1));
      if (prev && !prev.classList.contains('found')) {
        prev.classList.remove('checking');
        prev.classList.add('eliminated');
      }
    }

    if (i >= data.length) {
      status.textContent = `❌ "${target}" not found after ${data.length} comparisons`;
      status.style.background = 'rgba(255,107,107,0.2)';
      status.style.color = '#FF6B6B';
      document.getElementById('searchPlayBtn').disabled = false;
      return;
    }

    const el = document.getElementById('si-' + i);
    el.classList.add('checking');
    status.textContent = `Checking index [${i}]: "${data[i]}" ${data[i].toLowerCase().includes(target.toLowerCase()) ? '✅ Match!' : ''}`;

    if (data[i].toLowerCase().includes(target.toLowerCase())) {
      el.classList.remove('checking');
      el.classList.add('found');
      status.textContent = `✅ Found "${data[i]}" at index [${i}] — ${i + 1} comparison(s)`;
      status.style.background = 'rgba(29,209,161,0.2)';
      status.style.color = '#1DD1A1';
      document.getElementById('searchPlayBtn').disabled = false;
      return;
    }

    i++;
    searchTimer = setTimeout(step, searchSpeed);
  }

  step();
}

function runBinarySearch(data, target) {
  let left = 0, right = data.length - 1;
  const status = document.getElementById('searchStatus');
  let comparisons = 0;

  function step() {
    // Clear previous highlights
    document.querySelectorAll('.search-item').forEach(el => {
      el.classList.remove('checking');
    });

    if (left > right) {
      status.textContent = `❌ "${target}" not found after ${comparisons} comparisons`;
      status.style.background = 'rgba(255,107,107,0.2)';
      status.style.color = '#FF6B6B';
      document.getElementById('searchPlayBtn').disabled = false;
      return;
    }

    const mid = Math.floor((left + right) / 2);
    comparisons++;
    const el = document.getElementById('si-' + mid);
    el.classList.add('checking');

    status.textContent = `Checking mid=[${mid}]: "${data[mid]}" (left=${left}, right=${right})`;

    if (data[mid].toLowerCase() === target.toLowerCase()) {
      el.classList.remove('checking');
      el.classList.add('found');
      status.textContent = `✅ Found "${data[mid]}" at index [${mid}] — ${comparisons} comparison(s)`;
      status.style.background = 'rgba(29,209,161,0.2)';
      status.style.color = '#1DD1A1';
      document.getElementById('searchPlayBtn').disabled = false;
      return;
    }

    searchTimer = setTimeout(() => {
      el.classList.remove('checking');
      if (data[mid].toLowerCase() < target.toLowerCase()) {
        // Eliminate left side
        for (let k = left; k <= mid; k++) {
          document.getElementById('si-' + k).classList.add('eliminated');
        }
        left = mid + 1;
      } else {
        // Eliminate right side
        for (let k = mid; k <= right; k++) {
          document.getElementById('si-' + k).classList.add('eliminated');
        }
        right = mid - 1;
      }
      searchTimer = setTimeout(step, searchSpeed);
    }, searchSpeed);
  }

  step();
}

// ═══════════════════════════════════════════════════════
//  SORTING VISUALIZER
// ═══════════════════════════════════════════════════════
let sortArr = [];
let sortSpeed = 80;
let sortRunning = false;
let sortStopped = false;

// Speed buttons
document.querySelectorAll('[data-sort-speed]').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('[data-sort-speed]').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    sortSpeed = parseInt(btn.dataset.sortSpeed);
  });
});

function generateArray(n = 20) {
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(Math.floor(Math.random() * 180) + 20);
  return arr;
}

function renderBars(arr, highlights = {}) {
  const container = document.getElementById('barsContainer');
  container.innerHTML = '';
  const maxVal = Math.max(...arr);
  arr.forEach((val, i) => {
    const bar = document.createElement('div');
    bar.className = 'bar';
    const h = (val / maxVal) * 100;
    bar.style.height = h + '%';

    let color;
    if (highlights.sorted && highlights.sorted.has(i)) {
      color = COLORS[8]; // green
      bar.classList.add('sorted');
    } else if (highlights.comparing && highlights.comparing.has(i)) {
      color = COLORS[2]; // yellow
      bar.classList.add('comparing');
    } else if (highlights.pivot !== undefined && highlights.pivot === i) {
      color = COLORS[4]; // pink
      bar.classList.add('pivot');
    } else {
      const ci = Math.floor((val / 200) * (COLORS.length - 1));
      color = COLORS[ci];
    }

    bar.style.background = `linear-gradient(180deg, ${color}dd, ${color}66)`;
    bar.innerHTML = `<span class="bar-label">${val}</span>`;
    container.appendChild(bar);
  });
}

function resetSort() {
  sortStopped = true;
  sortRunning = false;
  sortArr = generateArray();
  renderBars(sortArr);
  document.getElementById('sortStatus').textContent = 'Press Play to start';
  document.getElementById('sortStatus').style.background = 'rgba(255,255,255,0.08)';
  document.getElementById('sortStatus').style.color = '';
  document.getElementById('sortPlayBtn').disabled = false;
  document.getElementById('sortPlayBtn').textContent = '▶️ Play';
  document.getElementById('sortPlayBtn').className = 'ctrl-btn play';
}

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function startSort() {
  if (sortRunning) return;
  sortRunning = true;
  sortStopped = false;
  document.getElementById('sortPlayBtn').disabled = true;
  const algo = document.getElementById('sortAlgoSelect').value;
  const status = document.getElementById('sortStatus');
  status.textContent = `Running ${algo} sort...`;

  const sorted = new Set();

  try {
    switch (algo) {
      case 'bubble':   await bubbleSortVisual(sorted);   break;
      case 'selection':await selectionSortVisual(sorted); break;
      case 'merge':    await mergeSortVisual();           break;
      case 'quick':    await quickSortVisual();           break;
    }
  } catch (e) {
    if (e === 'stopped') return;
  }

  if (!sortStopped) {
    // Mark all as sorted
    const allSorted = new Set(sortArr.map((_, i) => i));
    renderBars(sortArr, { sorted: allSorted });
    status.textContent = '🎉 Sorted! Well done!';
    status.style.background = 'linear-gradient(135deg, #1DD1A1, #00b894)';
    status.style.color = '#fff';
  }
  sortRunning = false;
  document.getElementById('sortPlayBtn').disabled = false;
}

function checkStopped() {
  if (sortStopped) throw 'stopped';
}

// ── BUBBLE SORT ──
async function bubbleSortVisual(sorted) {
  const n = sortArr.length;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      checkStopped();
      renderBars(sortArr, { comparing: new Set([j, j + 1]), sorted });
      await sleep(sortSpeed);
      if (sortArr[j] > sortArr[j + 1]) {
        [sortArr[j], sortArr[j + 1]] = [sortArr[j + 1], sortArr[j]];
        renderBars(sortArr, { comparing: new Set([j, j + 1]), sorted });
        await sleep(sortSpeed / 2);
      }
    }
    sorted.add(n - i - 1);
  }
}

// ── SELECTION SORT ──
async function selectionSortVisual(sorted) {
  const n = sortArr.length;
  for (let i = 0; i < n; i++) {
    let minIdx = i;
    for (let j = i + 1; j < n; j++) {
      checkStopped();
      renderBars(sortArr, { comparing: new Set([minIdx, j]), sorted });
      await sleep(sortSpeed);
      if (sortArr[j] < sortArr[minIdx]) minIdx = j;
    }
    [sortArr[i], sortArr[minIdx]] = [sortArr[minIdx], sortArr[i]];
    sorted.add(i);
    renderBars(sortArr, { sorted });
    await sleep(sortSpeed);
  }
}

// ── MERGE SORT ──
async function mergeSortVisual() {
  async function mergeSort(arr, l, r) {
    if (l >= r) return;
    checkStopped();
    const m = Math.floor((l + r) / 2);
    await mergeSort(arr, l, m);
    await mergeSort(arr, m + 1, r);
    await merge(arr, l, m, r);
  }

  async function merge(arr, l, m, r) {
    const left = arr.slice(l, m + 1);
    const right = arr.slice(m + 1, r + 1);
    let i = 0, j = 0, k = l;
    while (i < left.length && j < right.length) {
      checkStopped();
      renderBars(sortArr, { comparing: new Set([k]) });
      await sleep(sortSpeed);
      if (left[i] <= right[j]) {
        arr[k++] = left[i++];
      } else {
        arr[k++] = right[j++];
      }
      renderBars(sortArr);
    }
    while (i < left.length) { arr[k++] = left[i++]; renderBars(sortArr); await sleep(sortSpeed / 3); checkStopped(); }
    while (j < right.length) { arr[k++] = right[j++]; renderBars(sortArr); await sleep(sortSpeed / 3); checkStopped(); }
  }

  await mergeSort(sortArr, 0, sortArr.length - 1);
}

// ── QUICK SORT ──
async function quickSortVisual() {
  async function qs(arr, low, high) {
    if (low >= high) return;
    checkStopped();
    const pi = await partition(arr, low, high);
    await qs(arr, low, pi - 1);
    await qs(arr, pi + 1, high);
  }

  async function partition(arr, low, high) {
    const pivot = arr[high];
    let i = low - 1;
    for (let j = low; j < high; j++) {
      checkStopped();
      renderBars(sortArr, { comparing: new Set([j, high]), pivot: high });
      await sleep(sortSpeed);
      if (arr[j] < pivot) {
        i++;
        [arr[i], arr[j]] = [arr[j], arr[i]];
        renderBars(sortArr, { comparing: new Set([i, j]), pivot: high });
        await sleep(sortSpeed / 2);
      }
    }
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
    renderBars(sortArr, { comparing: new Set([i + 1]) });
    await sleep(sortSpeed);
    return i + 1;
  }

  await qs(sortArr, 0, sortArr.length - 1);
}

// ═══════════════════════════════════════════════════════
//  BIG O VISUAL BARS (Overview tab)
// ═══════════════════════════════════════════════════════
function renderBigOBars() {
  const container = document.getElementById('bigo-bars');
  if (!container) return;
  const data = [
    { label: 'O(1)', desc: 'Constant', width: 5, color: '#1DD1A1' },
    { label: 'O(log n)', desc: 'Logarithmic', width: 12, color: '#00D2D3' },
    { label: 'O(n)', desc: 'Linear', width: 30, color: '#FECA57' },
    { label: 'O(n log n)', desc: 'Linearithmic', width: 55, color: '#FF9F43' },
    { label: 'O(n²)', desc: 'Quadratic', width: 85, color: '#FF6B6B' },
    { label: 'O(2ⁿ)', desc: 'Exponential', width: 100, color: '#c0392b' },
  ];

  container.innerHTML = data.map((d, i) => `
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;animation:fadeInUp 0.4s ease-out ${i * 0.08}s both">
      <span style="min-width:80px;font-size:13px;font-weight:700;font-family:'JetBrains Mono',monospace;color:${d.color}">${d.label}</span>
      <div style="flex:1;height:22px;border-radius:11px;background:rgba(255,255,255,0.06);overflow:hidden">
        <div style="width:${d.width}%;height:100%;border-radius:11px;background:linear-gradient(90deg,${d.color}dd,${d.color}66);transition:width 1s ease-out"></div>
      </div>
      <span style="min-width:100px;font-size:12px;color:var(--text-muted)">${d.desc}</span>
    </div>
  `).join('');
}

// ═══════════════════════════════════════════════════════
//  INIT
// ═══════════════════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  renderBigOBars();
  resetSort();
  resetSearch();
});

