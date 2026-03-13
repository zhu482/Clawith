import { useEffect, useRef, useState } from 'react';
import { useTaskStore, type TaskStatus } from '../stores';
import './LobsterStatus.css';

const STORAGE_KEY = 'lobster-pos';

function getSavedPos() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) return JSON.parse(raw) as { x: number; y: number };
  } catch { /* ignore */ }
  return { x: window.innerWidth - 90, y: window.innerHeight - 90 };
}

/* ── 小龙虾 SVG ── */
function LobsterSVG({ status }: { status: TaskStatus }) {
  return (
    <svg viewBox="0 0 72 80" xmlns="http://www.w3.org/2000/svg" className={`lobster-svg lobster-${status}`}>
      {/* 尾扇 */}
      <ellipse cx="36" cy="72" rx="12" ry="6" fill="#c0392b" opacity="0.8" className="lobster-tail" />
      <ellipse cx="24" cy="74" rx="7" ry="4" fill="#c0392b" opacity="0.7" transform="rotate(-20 24 74)" className="lobster-tail" />
      <ellipse cx="48" cy="74" rx="7" ry="4" fill="#c0392b" opacity="0.7" transform="rotate(20 48 74)" className="lobster-tail" />

      {/* 腹节 */}
      <rect x="28" y="48" width="16" height="6" rx="3" fill="#e74c3c" />
      <rect x="27" y="54" width="18" height="6" rx="3" fill="#c0392b" />
      <rect x="28" y="60" width="16" height="6" rx="3" fill="#e74c3c" />
      <rect x="29" y="66" width="14" height="6" rx="3" fill="#c0392b" />

      {/* 身体/头胸甲 */}
      <ellipse cx="36" cy="36" rx="16" ry="20" fill="#e74c3c" />
      <ellipse cx="36" cy="34" rx="13" ry="16" fill="#ec7063" />

      {/* 眼睛 */}
      <circle cx="29" cy="24" r="4" fill="#1a1a1a" />
      <circle cx="43" cy="24" r="4" fill="#1a1a1a" />
      <circle cx="30" cy="23" r="1.5" fill="white" />
      <circle cx="44" cy="23" r="1.5" fill="white" />

      {/* 触须 */}
      <line x1="28" y1="21" x2="10" y2="8" stroke="#c0392b" strokeWidth="1.5" strokeLinecap="round" className="lobster-antenna-l" />
      <line x1="44" y1="21" x2="62" y2="8" stroke="#c0392b" strokeWidth="1.5" strokeLinecap="round" className="lobster-antenna-r" />
      <line x1="28" y1="22" x2="14" y2="4" stroke="#e74c3c" strokeWidth="1" strokeLinecap="round" className="lobster-antenna-l" />
      <line x1="44" y1="22" x2="58" y2="4" stroke="#e74c3c" strokeWidth="1" strokeLinecap="round" className="lobster-antenna-r" />

      {/* 大螯 左 */}
      <g className="lobster-claw-l">
        <line x1="22" y1="34" x2="8" y2="28" stroke="#c0392b" strokeWidth="3" strokeLinecap="round" />
        <ellipse cx="5" cy="26" rx="6" ry="4" fill="#e74c3c" transform="rotate(-30 5 26)" />
        <line x1="3" y1="22" x2="7" y2="28" stroke="#c0392b" strokeWidth="1.5" strokeLinecap="round" />
      </g>

      {/* 大螯 右 */}
      <g className="lobster-claw-r">
        <line x1="50" y1="34" x2="64" y2="28" stroke="#c0392b" strokeWidth="3" strokeLinecap="round" />
        <ellipse cx="67" cy="26" rx="6" ry="4" fill="#e74c3c" transform="rotate(30 67 26)" />
        <line x1="69" y1="22" x2="65" y2="28" stroke="#c0392b" strokeWidth="1.5" strokeLinecap="round" />
      </g>

      {/* 步足 左侧 */}
      <line x1="24" y1="38" x2="12" y2="44" stroke="#c0392b" strokeWidth="1.5" strokeLinecap="round" className="lobster-leg-l1" />
      <line x1="22" y1="42" x2="10" y2="50" stroke="#c0392b" strokeWidth="1.5" strokeLinecap="round" className="lobster-leg-l2" />
      <line x1="22" y1="46" x2="11" y2="56" stroke="#c0392b" strokeWidth="1.5" strokeLinecap="round" className="lobster-leg-l3" />

      {/* 步足 右侧 */}
      <line x1="48" y1="38" x2="60" y2="44" stroke="#c0392b" strokeWidth="1.5" strokeLinecap="round" className="lobster-leg-r1" />
      <line x1="50" y1="42" x2="62" y2="50" stroke="#c0392b" strokeWidth="1.5" strokeLinecap="round" className="lobster-leg-r2" />
      <line x1="50" y1="46" x2="61" y2="56" stroke="#c0392b" strokeWidth="1.5" strokeLinecap="round" className="lobster-leg-r3" />

      {/* 状态装饰 */}
      {status === 'done' && (
        <g className="lobster-stars">
          <text x="52" y="14" fontSize="10">⭐</text>
          <text x="8" y="12" fontSize="8">✨</text>
        </g>
      )}
      {status === 'error' && (
        <text x="28" y="12" fontSize="14" className="lobster-error-mark">!</text>
      )}
      {status === 'working' && (
        <g className="lobster-sweat">
          <text x="54" y="18" fontSize="9">💦</text>
        </g>
      )}
    </svg>
  );
}

const statusLabel: Record<TaskStatus, string> = {
  idle:    '待命中',
  working: '执行任务中...',
  done:    '任务完成！',
  error:   '任务中断',
};

const statusColor: Record<TaskStatus, string> = {
  idle:    '#888',
  working: '#facc15',
  done:    '#4ade80',
  error:   '#f87171',
};

export default function LobsterStatus() {
  const { status } = useTaskStore();

  const [pos, setPos] = useState(getSavedPos);
  const [showTooltip, setShowTooltip] = useState(false);
  const isDragging = useRef(false);
  const dragOffset = useRef({ x: 0, y: 0 });
  const hasMoved = useRef(false);
  const containerRef = useRef<HTMLDivElement>(null);

  // Clamp to viewport
  const clamp = (x: number, y: number) => ({
    x: Math.max(0, Math.min(window.innerWidth - 72, x)),
    y: Math.max(0, Math.min(window.innerHeight - 80, y)),
  });

  const onMouseDown = (e: React.MouseEvent) => {
    isDragging.current = true;
    hasMoved.current = false;
    dragOffset.current = { x: e.clientX - pos.x, y: e.clientY - pos.y };
    e.preventDefault();
  };

  useEffect(() => {
    const onMove = (e: MouseEvent) => {
      if (!isDragging.current) return;
      hasMoved.current = true;
      const next = clamp(e.clientX - dragOffset.current.x, e.clientY - dragOffset.current.y);
      setPos(next);
    };
    const onUp = () => {
      if (isDragging.current) {
        isDragging.current = false;
        localStorage.setItem(STORAGE_KEY, JSON.stringify(pos));
      }
    };
    window.addEventListener('mousemove', onMove);
    window.addEventListener('mouseup', onUp);
    return () => {
      window.removeEventListener('mousemove', onMove);
      window.removeEventListener('mouseup', onUp);
    };
  }, [pos]);

  // Tooltip auto-hide
  useEffect(() => {
    if (status === 'done' || status === 'error') {
      setShowTooltip(true);
      const t = setTimeout(() => setShowTooltip(false), 2800);
      return () => clearTimeout(t);
    }
  }, [status]);

  const handleClick = () => {
    if (!hasMoved.current) setShowTooltip(v => !v);
  };

  return (
    <div
      ref={containerRef}
      className={`lobster-widget lobster-state-${status}`}
      style={{ left: pos.x, top: pos.y }}
      onMouseDown={onMouseDown}
      onClick={handleClick}
    >
      <LobsterSVG status={status} />

      {/* 状态指示灯 */}
      <div className="lobster-dot" style={{ background: statusColor[status] }} />

      {/* tooltip */}
      {showTooltip && (
        <div className="lobster-tooltip">
          <span className="lobster-tooltip-text">{statusLabel[status]}</span>
        </div>
      )}
    </div>
  );
}
